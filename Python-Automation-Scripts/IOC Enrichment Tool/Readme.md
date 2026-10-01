# IOC Enrichment Tool

The capstone project of the *Automate the Boring Stuff* progression in this portfolio: a single CLI tool that reads a real log file, extracts indicators of compromise with regex, enriches IPs with real threat intelligence via the AbuseIPDB API, and exports a structured report to CSV and/or JSON.

This project ties together every technique practiced in the earlier scripts in this folder — [`Pattern Extractor CLI`](../Pattern%20Extractor%20CLI), [`Pattern Extractor Path`](../Pattern%20Extractor%20Path), and [`Log Enricher`](../Log%20Enricher) — into one finished tool.

## What it does

1. Reads a log file passed as a command-line argument, with clear error handling for a missing or unreadable file
2. Extracts, from the raw log text:
   - IPv4 addresses (deduplicated, octet-range validated)
   - Email addresses (validated to not swallow trailing sentence punctuation)
   - Timestamps (calendar-validated with `datetime.strptime`, not just format-matched)
3. Filters out private/local IP ranges before querying any external API
4. Enriches each remaining public IP against the [AbuseIPDB](https://www.abuseipdb.com/) API, classifying it as Clean, Suspicious, or Malicious based on its real abuse confidence score
5. Exports the results as CSV, JSON, or both — the JSON report is hierarchical, separating metadata (event counts, detected emails) from the network indicators table

## Usage

```bash
# Using an API key passed directly
python ioc-enrichment.py server_log.txt --apikey YOUR_KEY

# Using an API key stored in an environment variable (recommended)
setx ABUSEIPDB_KEY "YOUR_KEY"      # Windows, persists across sessions
python ioc-enrichment.py server_log.txt

# Choosing the export format
python ioc-enrichment.py server_log.txt --formato csv
python ioc-enrichment.py server_log.txt --formato json
python ioc-enrichment.py server_log.txt --formato ambos   # default
```

Output files are named automatically from the input log (e.g. `server_log.txt` → `server_log_reporte.json` / `server_log_reporte_ips.csv`).

## Security note on the API key

The API key can be passed via `--apikey`, but the recommended path is the `ABUSEIPDB_KEY` environment variable — passing secrets as CLI arguments leaves them exposed in shell history and to any process listing. For a personal portfolio project, an environment variable (even a persistent one via `setx`) is a reasonable trade-off; a production environment would use a proper secrets manager instead.

## Concepts practiced

- Combining regex extraction, external API enrichment, and file I/O in a single pipeline — the full chain from raw log to structured report
- `argparse` with a required positional argument and optional flags (`--formato`, `--apikey`)
- Reading credentials from an environment variable with a CLI override, instead of hardcoding or requiring a flag
- Deduplicating and pre-filtering data (private IP ranges) before making external API calls, to conserve rate limits
- Writing both flat (CSV via `csv.DictWriter`) and nested (JSON) structured output from the same underlying data
- Per-item error handling so one failed API call doesn't stop the rest of the batch

## Known limitations

- The private-IP filter is a simple prefix check (`192.168.`, `10.`, `127.`, `172.`) rather than full CIDR-aware matching — it covers the common cases but isn't exhaustive for all of `172.16.0.0/12`.
- No caching between runs — re-running against the same log re-queries the API for every IP, which matters given AbuseIPDB's free-tier rate limit.

## Requirements

- Python 3.10+
- `requests` — `pip install requests`
- A free [AbuseIPDB](https://www.abuseipdb.com/) account and API key

## Files

- `ioc-enrichment.py` — main script
- `server_log.txt` — sample log file used for testing
- `server_log_reporte.json` — example output from a test run