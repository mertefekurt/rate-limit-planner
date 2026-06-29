# rate-limit-planner

`rate-limit-planner` is a small local CLI that review API workload notes for missing rate limits, retries, and backoff.

## Why it is useful

Automation jobs and LLM apps often fail under vendor limits. This CLI flags workload plans without backoff and concurrency controls.

## Key features

- reads text, JSON, JSONL, or CSV inputs
- returns Markdown or JSON reports
- supports severity-based CI exit codes
- keeps all checks deterministic and offline
- includes focused rules for this project:
- `unbounded-concurrency`: concurrency is unbounded
- `retry-forever`: retry policy is unbounded
- `missing-backoff`: backoff is missing

## Installation

```bash
python -m pip install -e ".[dev]"
```

## Usage

```bash
rate-limit-planner examples/sample.txt
rate-limit-planner examples/sample.txt --json
rate-limit-planner path/to/input.txt --fail-on medium --out report.md
python -m rate_limit_planner --help
```

Example input:

```text
send 10000 requests concurrency: unlimited retry forever no backoff
```

## CLI options

```text
rate-limit-planner INPUT [--format auto|text|jsonl|csv|json] [--json]
             [--fail-on low|medium|high] [--out PATH]
```

`INPUT` is any API workload plan or integration notes. The tool exits with code `2` when findings meet the selected
threshold, which makes it easy to use in GitHub Actions or release checks.

## Workflow

```mermaid
flowchart LR
    A[input file] --> B[format reader]
    B --> C[project-specific rules]
    C --> D[risk score]
    D --> E[Markdown or JSON report]
```

## Tests

```bash
ruff check .
pytest
python -m rate_limit_planner --help
```

## License

MIT
