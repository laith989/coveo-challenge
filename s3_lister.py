from datetime import datetime

import boto3
from concurrent.futures import ThreadPoolExecutor, as_completed
from dateutil.tz import tzutc
from collections import defaultdict
from utils import  print_table, calculate_cost, filter_objects_by_storage_class, format_size, matches_name, group_by_encryption


s3 = boto3.resource("s3")
client = boto3.client("s3")


def summarize_buckets(bucket_name, storage_class, unit, group_by_region, group_by_encryption_type):
    buckets = s3.buckets.all()
    summaries = []

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = {
            executor.submit(get_bucket, bucket, bucket_name, storage_class, unit): bucket.name
            for bucket in buckets
        }
        for future in as_completed(futures):
            result = future.result()
            if result:
                summaries.append(result)
    # Compute total size in bytes across all buckets
    total_size_key = "Total Size ({})".format(unit.upper())
    total_size_bytes = sum(summary.get(total_size_key, 0) for summary in summaries)

    # Add percentage to each summary
    
    for summary in summaries:
        size = summary.get(total_size_key, 0)
        percent = (size / total_size_bytes * 100) if total_size_bytes else 0
        summary["Size % of Total"] = f"{percent:.2f}%"

    if group_by_region:
        grouped = defaultdict(list)
        for summary in summaries:
            grouped[summary["Region"]].append(summary)
        for region, group in grouped.items():
            print(f"\nRegion: {region}")
            print_table(group)
    elif group_by_encryption_type:
        grouped = group_by_encryption(summaries)
        for encryption, group in grouped.items():
            print(f"Encryption Type: {encryption}")
            print_table(group)
    else:
        print_table(summaries)


def get_bucket(bucket, bucket_name, storage_class, unit):
    name = bucket.name
    if bucket_name and not matches_name(name, bucket_name):
        return None

    paginator = client.get_paginator("list_object_versions")
    bucket_size = 0
    count = 0
    last_modified = datetime.min.replace(tzinfo=tzutc())
    cost = 0
    encryption_counts = defaultdict(int)
    storage_class_count = defaultdict(int)

    for page in paginator.paginate(Bucket=name):
        versions = page.get("Versions", [])
        delete_markers = page.get("DeleteMarkers", [])

        for obj in versions:
             # Filter by storage class if requested
            obj_storage_class = obj.get("StorageClass", "STANDARD")
            if storage_class and obj_storage_class.upper() != storage_class.upper():
                continue

            size = obj["Size"]
            bucket_size += size
            count += 1
            storage_class_count[obj_storage_class] += 1

            if (new_last_modified := obj["LastModified"]) > last_modified:
                last_modified = new_last_modified

            cost += calculate_cost(obj_storage_class, size)
            try:
                metadata = client.head_object(Bucket=name, Key=obj["Key"], VersionId=obj["VersionId"])
                encryption = metadata.get("ServerSideEncryption", "None")
            except Exception:
                encryption = "Unknown"

            encryption_counts[encryption] += 1

        count += len(delete_markers)

    try:
        client.get_bucket_lifecycle_configuration(Bucket=name)
        has_lifecycle = "✅"
    except client.exceptions.ClientError as e:
        if e.response["Error"]["Code"] == "NoSuchLifecycleConfiguration":
            has_lifecycle = "❌"
        else:
            has_lifecycle = "Error"

    try:
        client.get_bucket_replication(Bucket=name)
        has_replication = "✅"
    except client.exceptions.ClientError as e:
        if e.response["Error"]["Code"] == "ReplicationConfigurationNotFoundError":
            has_replication = "❌"
        else:
            has_replication = "Error"
            
    if storage_class and count == 0:
        return None

    return {
        "Bucket": name,
        "creation Date": (bucket.creation_date).strftime("%Y-%m-%d %H:%M:%S"),
        "Files": count,
        "Total Size ({})".format(unit.upper()): format_size(bucket_size, unit),
        "Last Modified": last_modified.strftime("%Y-%m-%d %H:%M:%S"),
        "Cost ($)": round(cost, 6),
        "Region": get_bucket_region(name),
        "Storage Class" : obj_storage_class,
        "Encryption Types": dict(encryption_counts), 
        "Has Lifecycle": has_lifecycle,
        "Has Replication": has_replication,
    }


def get_bucket_region(bucket_name):
    loc = client.get_bucket_location(Bucket=bucket_name)
    return loc.get("LocationConstraint") or "us-east-1"
