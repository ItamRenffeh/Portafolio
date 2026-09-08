# Security Incident Reports

This folder contains simulated security incident investigations, written as if produced by a SOC analyst during real-world triage. Each case walks through detection, SQL-based forensic analysis of audit logs, impact assessment, IoC extraction, and remediation recommendations.

The goal of these exercises is to practice the full investigative workflow — not just writing queries, but reasoning about attacker behavior, quantifying business impact, and producing recommendations a real organization could act on.

## Methodology

All investigations follow the same structure:

1. **Executive Summary** — what happened, at a glance
2. **Investigation Methodology** — SQL queries used to trace the attack, with reasoning for each step
3. **Timeline / Findings** — chronological reconstruction of the incident
4. **Impact Assessment** — quantified scope of data or systems affected
5. **Indicators of Compromise (IoCs)** — consolidated table for quick reference
6. **Remediation Recommendations** — immediate containment and longer-term hardening steps

## Cases

| # | Case | Attack Type | Key Skills Demonstrated |
|---|------|-------------|--------------------------|
| 01 | [Access Breach & Data Exfiltration](./01-Access-Breach-Data-Exfiltration) | Credential compromise → data exfiltration | Log correlation with `JOIN`, timeline reconstruction |
| 02 | [Brute-Force Attack & DB Exfiltration](./02-Bruteforce-Attack-DB-Exfiltration) | Brute-force login → account takeover → mass export | `GROUP BY`/`COUNT` for attack detection, time-windowed impact quantification with `SUM`/`BETWEEN` |

## Disclaimer

All data, usernames, IP addresses, and organizations referenced in these reports are fictional and created for practice purposes only.