# Modo Setup

A small script that automates the start of a daily study routine: it launches GitHub Desktop and opens a fixed set of browser tabs used for study sessions, so the whole setup is one command instead of several manual clicks.

## What it does

1. Locates and launches GitHub Desktop automatically, by building its install path from the `LOCALAPPDATA` environment variable (Windows) rather than hardcoding a username-specific path
2. Handles the case where GitHub Desktop isn't found at that path, printing the path it searched instead of crashing
3. Waits briefly to let GitHub Desktop start loading
4. Opens a fixed list of browser tabs (YouTube Music, Google, Gemini) used during study sessions

## Usage

```bash
python modo_setup.py
```

## Concepts practiced

- Reading environment variables (`os.environ`) to build portable file paths instead of hardcoding a specific user's directory
- Launching external applications from Python with `os.startfile()`
- Opening multiple browser tabs programmatically with `webbrowser`
- Basic error handling for a missing executable (`FileNotFoundError`)

## Known limitation

`os.startfile()` and the `LOCALAPPDATA`-based path are Windows-specific; this script won't run as-is on macOS/Linux.

## Files

- `modo_setup.py` — main script