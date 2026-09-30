# Pattern Extractor (File Path Version)

A variant of the [Pattern Extractor CLI](../Pattern%20Extractor%20CLI) that reads from a fixed log file on disk instead of the clipboard, built while working through *Automate the Boring Stuff* (chapter 10: Reading and Writing Files).

## What it does

1. Reads `log.txt` from the same directory as the script
2. Handles missing files or encoding issues with `try`/`except`, exiting cleanly with an error message instead of crashing
3. Extracts IPv4 addresses, email addresses, and calendar-validated timestamps using the same regex logic as the CLI version
4. Prints all three categories to the console

## Known gap vs. the original exercise

This version hardcodes the file path (`log.txt` next to the script) rather than accepting one as a command-line argument, and it still prints to the console instead of writing results to an output file. Chapter 12's `argparse`-based `--input`/`--output` interface is the next step to fully close this out — see [`Pattern Extractor CLI`](../Pattern%20Extractor%20CLI) for the in-progress version of that upgrade.

## Concepts practiced

- Reading a file from disk with `open()` inside a `try`/`except` block
- Using `pathlib.Path` to build a file path relative to the script's own location
- Reusing and extending regex/validation logic from earlier projects instead of rewriting it

## Files

- `patternExtractorPath.py` — main script
- `log.txt` — sample log file used as input (not included here — add your own test log alongside the script)