# IP Frequency Counter

A script that counts how many times each IP address appears in a list, validates IPv4 format before counting, and reports the most frequent one(s).

Built while working through *Automate the Boring Stuff* (chapters 6-8: Lists, Dictionaries, and Strings), as a follow-up to the earlier [IP Address Classifier](../IP%20Address%20Classifier) project.

## What it does

1. Takes a hardcoded list of IP addresses (intentionally including duplicates, whitespace, and malformed entries)
2. Validates each entry as a proper IPv4 address before counting it
3. Builds a frequency dictionary (`{ip: count}`) using pure dict operations — no `collections.Counter`
4. Prints results sorted from most to least frequent
5. Identifies the IP(s) with the highest count (handles ties)

## IPv4 validation rules

An entry is only counted if it:
- Splits into exactly 4 parts separated by dots
- Has all-numeric parts (rejects letters, empty segments, negative signs)
- Has every octet within the 0-255 range

This means malformed input like `192.168.1`, `192.168.1.1.1`, `256.168.1.1`, `-1.168.1.1`, or empty strings are silently excluded from the count rather than crashing the script.

**Known limitation:** addresses with leading zeros (e.g. `192.168.001.1`) currently pass validation, since the check only looks at numeric range, not formatting strictness. Left as-is for this exercise.

## Concepts practiced

- Dictionary accumulator pattern (`dict.get(key, 0) + 1`)
- Sorting a dictionary by value with `sorted()` + `lambda`
- List comprehensions (input validation, finding all ties for the max)
- String methods (`.strip()`, `.split()`, `.isdigit()`)
- Designing test data that deliberately covers edge cases, not just the happy path

## Example output

```
45.170.23.11: 4 veces
192.168.1.10: 3 veces
10.0.0.5: 2 veces
8.8.8.8: 2 veces
0.0.0.0: 2 veces
255.255.255.255: 1 veces

IP(s) más repetida(s): 45.170.23.11
```

## Files

- `ip_frequency_counter.py` — main script