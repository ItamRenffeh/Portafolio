# Pattern Extractor CLI

An upgraded version of the original [Pattern Extractor](../Pattern%20Extractor), built while working through *Automate the Boring Stuff* (chapters 10 and 12: Reading/Writing Files, CLI Programs). It reads real input — a file or the clipboard — instead of a hardcoded string, and validates timestamps against the actual calendar instead of just their format.

## What it does

1. Reads log text from either:
   - a file path passed as a command-line argument (`python PatterScrip.py logs.txt`), or
   - the system clipboard, if no file path is given
2. Extracts IPv4 addresses, email addresses, and timestamps using regex
3. Validates each timestamp against the real calendar with `datetime.strptime` — rejecting things like `2026-13-40` (invalid month/day) even when the digit *format* looks correct, which the earlier version could not do
4. Prints all three categories to the console

## Usage

```bash
# Analyze a file
python PatterScrip.py path/to/logfile.txt

# Analyze whatever is currently on the clipboard
python PatterScrip.py
```

## Known gap vs. the original exercise

Chapter 12 specifically introduces `argparse` for flag-based CLI tools (e.g. `--input file.txt --output results.txt`). This version instead reads a plain positional argument and prints results to the console rather than writing them to an output file. Functionally it works, but it doesn't yet use `argparse` or produce a file — that's the natural next iteration.

## Concepts practiced

- Reading files safely with `open()` inside a `try`/`except` block, handling both missing files and encoding errors
- Using `sys.argv` to accept a command-line argument
- Falling back to clipboard input (`pyperclip`) when no argument is given
- Calendar-aware date validation with `datetime.strptime`, closing a gap identified in the previous project (a syntactically valid but calendar-invalid date could previously slip through)
- Negative lookbehind/lookahead in regex (`(?<![\d.])`, `(?!\d|\.\d)`) to avoid partial matches inside longer numeric sequences

## Requirements

- Python 3.10+
- [`pyperclip`](https://pypi.org/project/pyperclip/) — install with `pip install pyperclip`

## Files

- `PatterScrip.py` — main script