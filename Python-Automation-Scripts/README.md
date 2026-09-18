# Python Automation Scripts

A collection of standalone Python scripts built while working through *Automate the Boring Stuff*, applied to networking and security use cases. Each subfolder is a self-contained project with its own README.

## Projects

| Project | Chapters | Focus |
|---|---|---|
| [`IP Address Classifier`](./IP%20Address%20Classifier) | 1-4 | Classifies IP addresses, with input validation via `try`/`except` |
| [`IP Frequency Counter`](./IP%20Frequency%20Counter) | 6-8 | Validates IPv4 format and counts frequency of occurrence using dictionaries |
| [`Pattern Extractor`](./Pattern%20Extractor) | 9 | Extracts IPs, emails, and timestamps from text using regular expressions |

Each project builds on the last — later scripts reuse and extend validation logic introduced earlier, rather than starting from scratch.

## Roadmap

These scripts are part of an ongoing progression tied to specific book chapters (file I/O, CLI tooling with `argparse`, and API integration are next). The end goal is a single integrated log-parsing tool that combines regex extraction, file I/O, and IP reputation lookups via a public API.

## Requirements

Python 3.10+. No external dependencies beyond the standard library so far — any script that needs one will note it in its own README.
