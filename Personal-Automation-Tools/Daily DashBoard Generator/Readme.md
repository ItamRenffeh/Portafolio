# Daily Dashboard Generator

A script that pulls together weather, currency exchange rates, GitHub trending repos, and news headlines into a single generated HTML page, then opens it in the browser. Built as a personal daily-briefing tool, combining several data-fetching techniques in one project.

## What it does

1. Fetches data from four different kinds of sources in parallel "blocks":
   - **Weather** — JSON API ([wttr.in](https://wttr.in))
   - **Currency rates** — JSON API ([dolarapi.com](https://dolarapi.com), Argentine peso exchange rates: Oficial, Blue, MEP)
   - **GitHub Trending (Python)** — HTML scraping with `BeautifulSoup` and CSS selectors
   - **News** — RSS/XML feeds (The Hacker News, ESET, Google News Argentina/World) parsed with `xml.etree.ElementTree`
2. Each data source has its own isolated `try`/`except` — if one fails, it shows an error card instead of crashing the whole dashboard
3. Assembles all the blocks into a single styled HTML page (dark theme, responsive grid layout)
4. Writes the page to disk and opens it automatically in the default browser

## Usage

```bash
# Default city (Bahía Blanca)
python tablero_web.py

# Custom city for the weather block
python tablero_web.py Buenos Aires
```

## Concepts practiced

- Consuming multiple, structurally different data sources in one program: REST/JSON, HTML scraping, and RSS/XML
- Parsing XML with `xml.etree.ElementTree` — a first in this portfolio, useful for the many security/news feeds that are RSS-based
- Per-source error isolation, so one failing API doesn't take down the whole tool ("graceful degradation")
- Generating dynamic HTML/CSS from Python and opening it programmatically with `webbrowser`
- Building a file path relative to the script's own location with `pathlib.Path`

## Requirements

- Python 3.10+
- `requests` — `pip install requests`
- `beautifulsoup4` — `pip install beautifulsoup4`

## Files

- `tablero_web.py` — main script