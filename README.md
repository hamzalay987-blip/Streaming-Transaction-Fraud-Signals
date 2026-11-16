# Incremental API-to-Warehouse Ingestion

Simulates a paginated operational API with idempotent upserts and cursor-based incremental ingestion.  
Persists watermarks in SQLite so reruns update changed records without introducing duplicates.

## Problem

API sources may paginate results and deliver updated records, making full reloads expensive and error-prone.

## Solution and design

Ingest ordered pages, apply versioned records with upsert semantics, and persist the high-watermark.

**Stack:** Python, REST pagination patterns, SQLite, incremental ETL

## Quick start

Requires Python 3.11+ (standard library only for the local demo).

```bash
python main.py
python -m unittest discover -s tests -v
```

A GitHub Actions workflow runs the same tests on pushes and pull requests.

## Project layout

- `main.py`: core processing and a small command-line demonstration
- `data/`, `seeds/`, `models/`, `sql/`, `infra/`, `dags/` or `powerbi/`: included only where relevant
- `tests/`: fixture-based expected-value and repeatability checks

## Engineering decisions

- Narrow scope, realistic field names, and synthetic reproducible inputs
- No credentials, customer records, patient data, API tokens, or paid cloud resources
- Visible business logic and deterministic fixtures rather than screenshots of unverifiable dashboards

## Limits and next iteration

Offline API fixture; production integration should implement HTTP retries, rate limits, and transactional cursor checkpoints.

A production hardening path would add larger-scale fixtures, alerting, operational runbooks, robust error handling, and integration tests against the real deployment target.

## Portfolio integrity

This is an independently reproducible **portfolio demonstration**, not a claim that these files are employer code or that a cloud workload has been deployed. The fixture data is synthetic.
