# Rate Limit Planner

> A small command-line review pass for rate limits.

![Rate Limit Planner cover](assets/readme-cover.svg)

Review API workload notes for missing rate limits, retries, and backoff. The repository is intentionally plain: a small command, a visible rule surface, and enough examples to make the behavior inspectable.

## Signals in plain English

- `unbounded-concurrency` (high): concurrency is unbounded. Fix: Set max concurrency and queue behavior..
- `retry-forever` (medium): retry policy is unbounded. Fix: Use bounded retries with jitter..
- `missing-backoff` (low): backoff is missing. Fix: Add exponential backoff and retry-after handling..

## Input and report

The reader accepts text, JSON, JSONL, or CSV. The default report is readable in a terminal or pull request; `--json` keeps the same findings available to automation.

## Demo

```bash
git clone https://github.com/mertefekurt/rate-limit-planner.git
cd rate-limit-planner
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
rate-limit-planner examples/sample.txt
rate-limit-planner examples/sample.txt --json
```

## Sanity checks

```bash
ruff check .
pytest
python -m rate_limit_planner --help
```
