# Log Enricher

A script that scrapes a public threat-intel feed for IP addresses and enriches each one with network/geolocation context, built while working through *Automate the Boring Stuff* (chapter 13: Web Scraping).

## What it does

1. Fetches a public IP blocklist feed ([abuse.ch Feodo Tracker](https://feodotracker.abuse.ch/), a list of active botnet/C2 IPs) using `requests`
2. Parses the page text with `BeautifulSoup` and extracts all IPv4 addresses via regex
3. Filters out private, loopback, and multicast ranges using Python's `ipaddress` module, keeping only public IPs worth investigating
4. Queries the free [ip-api.com](https://ip-api.com/) API for each IP to enrich it with country, city, ISP/organization, ASN, and whether the address belongs to a hosting/datacenter provider
5. Prints a formatted table of the results, respecting the API's rate limit with a short delay between requests

## Note on "enrichment" vs. "reputation"

The original project description called for reputation lookups (e.g. via AbuseIPDB). This version instead enriches IPs with **network and geolocation context** (ISP, ASN, hosting/datacenter flag) rather than an abuse/reputation score, since `ip-api.com` doesn't provide one on the free tier. The "is this a datacenter/hosting IP" flag is still useful signal in threat hunting — hosting-range IPs are more likely to be attacker infrastructure than residential ones — but it's a different kind of signal than a reputation score. A natural next step would be adding an AbuseIPDB lookup (free tier, requires an API key) alongside this.

## Concepts practiced

- Making HTTP requests with custom headers (`requests`)
- Parsing HTML/text content with `BeautifulSoup`
- Validating and filtering IP addresses with the standard library `ipaddress` module (`is_private`, `is_loopback`, `is_multicast`)
- Consuming a JSON API and handling both network errors and unsuccessful API responses
- Respecting a third-party API's rate limit with `time.sleep()`

## Requirements

- Python 3.10+
- `requests` — `pip install requests`
- `beautifulsoup4` — `pip install beautifulsoup4`

## Files

- `log_enricher.py` — main script