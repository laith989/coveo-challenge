# S3 Bucket Analyzer CLI

A command-line tool to inspect AWS S3 buckets and summarize their contents, cost, and configuration.

---

## Features

- List and analyze all or filtered S3 buckets
- Count object versions and storage sizes
- Filter by storage class (e.g., STANDARD, IA, RR)
- Group by region or encryption type
- Show:
  - Bucket name
  - Creation date
  - Number of files
  - Total size
  - Last modified date
  - Cost estimate
  - Region
  - Storage Class
  - Encryption breakdown
  - Lifecycle & replication status
  - Percentage of total space used

---

## Requirements

- Python 3.8 - 3.10
- [Poetry](https://python-poetry.org/) for dependency management
- AWS credentials configured (via `~/.aws/credentials` or environment variables)

Install dependencies:

```bash
$ poetry env use python3.10
$ poetry install --no-root
```

---

## Usage

```bash
poetry run python main.py [OPTIONS]
```

### Options
```
--bucket                    # Filter by bucket name (supports wildcards)
--storage-class             # Filter by object storage class (e.g., STANDARD, IA)
--unit                      # Display units: bytes, kb, mb, gb
--group-by-region           # Group output by AWS region
--group-by-encryption-type  # Group output by encryption type

```

### Example

```bash
poetry run python main.py --unit gb --group-by-region --storage-class STANDARD
```

---

## Output

The CLI prints a summary table like:

![alt text](<Screenshot 2025-03-26 at 5.06.59 PM.png>)

---

## ✅ Tips

- Make sure your AWS credentials are valid
- Use `--storage-class` to limit the analysis to cold storage tiers
- Combine `--group-by-region` and `--group-by-encryption-type` for full insights

---

