# Case 02 — Brute-Force Attack & DB Exfiltration

**Type:** Brute-force login attempt → account takeover → mass data export
**Status:** Contained / Mitigated

## Summary

An automated brute-force attack against the logistics platform's login portal succeeded in compromising an administrative account. The attacker used the account to scrape the internal database, exfiltrating approximately 9,790 records combining customer PII and operational route data.

## What this demonstrates

- Detecting brute-force activity by aggregating failed login attempts per IP (`GROUP BY` / `COUNT`)
- Confirming account compromise by correlating the attacking IP with a successful login
- Quantifying breach impact with a time-windowed aggregation query (`SUM` + `BETWEEN`) instead of an estimate
- Building a consolidated IoC table for fast handoff to other analysts
- Recommending both technical remediation (blocklisting, rate limiting) and compliance action (legal notification for PII exposure)

## Files

- `reporte.pdf` — full incident report