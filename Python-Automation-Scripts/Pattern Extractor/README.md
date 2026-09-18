# Pattern Extractor

A script that extracts IP addresses, email addresses, and timestamps from a block of text using regular expressions.

Built while working through *Automate the Boring Stuff* (chapter 9: Regular Expressions), as a follow-up to the earlier [IP Frequency Counter](../IP%20Frequency%20Counter) project.

## What it does

1. Takes a block of text (still a hardcoded string, not a file — that comes in the next project)
2. Extracts every IPv4 address, email address, and timestamp found in it using `re.findall()`
3. Prints each category separately
4. Includes a second "noisy" test block with edge cases (invalid IPs, malformed emails, multiple date formats, out-of-range times) to validate the patterns hold up under messy input

## Pattern design

- **IPs** — bounds each octet to 0-255 directly in the regex (`25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d`), so invalid addresses like `999.300.1.2` are rejected by the pattern itself rather than by a separate validation step.
- **Emails** — standard `local@domain.tld` pattern, requiring a valid-looking TLD (rejects addresses like `user@company` with no domain extension).
- **Timestamps** — supports both `YYYY-MM-DD` and `YYYY/MM/DD` date formats, `HH:MM:SS` with valid hour/minute/second ranges, and optional ISO 8601 extras (`T` separator, `Z` suffix, or a `+HH:MM` / `-HH:MM` timezone offset).

## Known limitation

The date portion of the timestamp pattern checks digit *count* (`\d{2}`) but not digit *range* for month and day — it doesn't reject an invalid date like `2026-13-40` on its own. In practice this is usually caught because the time portion of the same timestamp has to be valid too, but a timestamp with an invalid month/day paired with a *valid* time (e.g. `2026-13-40 12:30:00`) would still match. Left as-is for this exercise; a stricter version would need explicit month (`0[1-9]|1[0-2]`) and day ranges.

## Concepts practiced

- `re.findall()` for extracting all matches rather than just the first
- Raw strings (`r"..."`) for regex patterns
- Building a complex pattern from smaller reusable pieces (e.g. the `octet` sub-pattern reused via an f-string)
- Non-capturing groups (`(?:...)`) and lookahead (`(?!\w)`) to keep matches precise without polluting `findall()` output
- Designing adversarial test input to find the edges of your own pattern, not just confirm the happy path

