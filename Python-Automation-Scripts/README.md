# Python Automation Scripts

A collection of standalone Python scripts built while working through *Automate the Boring Stuff*, applied to networking and security use cases. Each subfolder is a self-contained project with its own README.

## Projects

| Project | Chapters | Focus |
|---|---|---|
| [`IP Address Classifier`](./IP%20Address%20Classifier) | 1-4 | Classifies IP addresses, with input validation via `try`/`except` |
| [`IP Frequency Counter`](./IP%20Frequency%20Counter) | 6-8 | Validates IPv4 format and counts frequency of occurrence using dictionaries |
| [`Pattern Extractor`](./Pattern%20Extractor) | 9 | Extracts IPs, emails, and timestamps from text using regular expressions |
| [`Pattern Extractor CLI`](./Pattern%20Extractor%20CLI) | 10, 12 | Reads from a file or clipboard, with calendar-validated timestamps |
| [`Pattern Extractor (File Path Version)`](./Pattern%20Extractor%20Path) | 10 | Reads directly from a log file on disk with error handling |
| [`Log Enricher`](./Log%20Enricher) | 13 | Scrapes a public threat feed and enriches extracted IPs with geolocation/network data via a public API |
| [`IOC Enrichment Tool`](./IOC%20Enrichment%20Tool) | 9, 10, 12, 13, 18 | **Capstone project** — full pipeline: reads a log file, extracts IOCs with regex, enriches IPs via the AbuseIPDB threat intel API, and exports a structured CSV/JSON report |

Each project builds on the last — later scripts reuse and extend validation logic introduced earlier, rather than starting from scratch. The IOC Enrichment Tool is the integration point where all of it comes together into one finished tool.

## Requirements

Python 3.10+. Some scripts need external packages (`requests`, `beautifulsoup4`, `pyperclip`) and, for the capstone project, a free AbuseIPDB API key — check each project's own README for exact dependencies.