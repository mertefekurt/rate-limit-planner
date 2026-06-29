from __future__ import annotations

from rate_limit_planner.models import Rule

PROJECT_NAME = 'rate-limit-planner'
DESCRIPTION = 'Review API workload notes for missing rate limits, retries, and backoff.'
TEXT_FIELDS = ("text", "content", "description", "summary", "body", "notes", "message")
SUBJECT_FIELDS = ("id", "name", "service", "dataset", "route", "metric", "field", "path")
HIGH_SAMPLE = 'send 10000 requests concurrency: unlimited retry forever no backoff'
MEDIUM_SAMPLE = '\\b(retry forever|retries\\s*[:=]\\s*unlimited)\\b'
CLEAN_SAMPLE = 'send 1000 requests concurrency 5 retry 3 exponential backoff rate_limit 60/min'

RULES = (
    Rule(
        code='unbounded-concurrency',
        severity='high',
        pattern='\\b(concurrency\\s*[:=]\\s*(unlimited|none)|parallel unlimited)\\b',
        message='concurrency is unbounded',
        recommendation='Set max concurrency and queue behavior.',
    ),
    Rule(
        code='retry-forever',
        severity='medium',
        pattern='\\b(retry forever|retries\\s*[:=]\\s*unlimited)\\b',
        message='retry policy is unbounded',
        recommendation='Use bounded retries with jitter.',
    ),
    Rule(
        code='missing-backoff',
        severity='low',
        pattern='\\b(no backoff|backoff\\s*[:=]\\s*(none|missing))\\b',
        message='backoff is missing',
        recommendation='Add exponential backoff and retry-after handling.',
    ),
)
