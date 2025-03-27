from typing import Optional

import typer
from tabulate import tabulate

from s3_lister import summarize_buckets


def print_as_table(bucket_information):
    print(tabulate(bucket_information, headers="keys"))


def main(
        # --bucket
        bucket: Optional[str] = typer.Option(None, help="Bucket names"),
        # --storage-class
        storage_class: Optional[str] = typer.Option(None, help="Filter objects by storage class (e.g., STANDARD, IA)"),
        # --unit
        unit: str = typer.Option("mb", help="Display size in bytes, kb, mb, or gb"),
        # --group-by-region
        group_by_region: bool = typer.Option(False, help="Group output by region"),
        # --group-by-encryption-type
        group_by_encryption_type: bool = typer.Option(False, help="Group output by dominant encryption type")

):
    summarize_buckets(bucket, storage_class, unit, group_by_region, group_by_encryption_type)


if __name__ == "__main__":
    typer.run(main)
