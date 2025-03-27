from tabulate import tabulate
from fnmatch import fnmatch
from collections import defaultdict


def matches_name(name, pattern):
    return fnmatch(name, pattern)

def format_size(bytes_value, unit='mb'):
    units = {
        'bytes': 1,
        'kb': 1024,
        'mb': 1024 ** 2,
        'gb': 1024 ** 3,
    }
    return round(bytes_value / units.get(unit.lower(), 1024 ** 2), 3)

def print_table(data):
    print(tabulate(data, headers="keys"))


def filter_objects_by_storage_class(objects, target_class):
    return [obj for obj in objects if obj.get("StorageClass") == target_class]



def calculate_cost(storage_class, size_bytes):
    price_per_gb = {
        "STANDARD": 0.023,
        "STANDARD_IA": 0.0125,
        "ONEZONE_IA": 0.01,
        "GLACIER": 0.004,
        "DEEP_ARCHIVE": 0.00099,
    }
    return (size_bytes / 1024 / 1024 / 1024) * price_per_gb.get(storage_class.upper(), 0.023)




def group_by_encryption(buckets):
    grouped = defaultdict(list)
    for bucket in buckets:
        enc_stats = bucket.get("Encryption Types", {})
        if not enc_stats:
            key = "Unknown"
        else:
            # Find the dominant encryption type
            key = max(enc_stats, key=enc_stats.get, default="Unknown")
        grouped[key].append(bucket)
    return grouped