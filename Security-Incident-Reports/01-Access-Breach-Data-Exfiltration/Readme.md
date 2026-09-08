# Case 01 — Access Breach & Data Exfiltration

**Type:** Compromised credentials → unauthorized data access → account lockout (denial of service)
**Status:** Contained / Mitigated

## Summary

An external attacker compromised a privileged user account with read/export access to a routing database. After gaining access, the attacker exfiltrated data and changed the account's credentials, locking out the legitimate user and confirming intent to maintain persistence.

## What this demonstrates

- Chronological log analysis to isolate an attack window
- Cross-referencing system logs with personnel records to assess who was affected
- Using `JOIN` to correlate failed login attempts (IP addresses) with real employee identities
- Translating technical findings into concrete remediation steps (firewall blocklisting, forced credential reset, MFA enforcement)

## Files

- `reporte.pdf` — full incident report