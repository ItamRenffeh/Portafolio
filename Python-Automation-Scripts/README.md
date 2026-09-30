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

Each project builds on the last — later scripts reuse and extend validation logic introduced earlier, rather than starting from scratch.

## Roadmap

Still pending: converting the file-reading scripts to use `argparse` with proper `--input`/`--output` flags and real file output (chapter 12 done right), then the final integrated project (chapter 18) — a single tool that reads a real log file, extracts patterns with regex, enriches with an API, and exports structured results to CSV/JSON.

## Requirements

Python 3.10+. Some scripts need external packages (`requests`, `beautifulsoup4`, `pyperclip`) — check each project's own README for exact dependencies.