# IP Address Classifier

Python script that classifies IPv4 addresses as private (RFC 1918) or 
public, with input validation to reject malformed addresses before 
classifying them.

## Files
- `ip_classifier.py` — main script
- `test-cases.png` — terminal output covering valid, boundary, and 
  malformed inputs

## How it works
- Prompts the user for how many IPs to check, then reads each one 
  from input
- Validates format first (exactly 4 octets, digits only, each in 
  0-255 range) — invalid input is rejected before any classification 
  logic runs
- Classifies valid IPs against the three RFC 1918 private ranges:
  - 10.0.0.0 – 10.255.255.255
  - 172.16.0.0 – 172.31.255.255
  - 192.168.0.0 – 192.168.255.255

## Test cases covered
- Private ranges: 10.x, 172.16-31.x, 192.168.x
- Range boundaries: 172.16.5.1 (valid, lower edge) and 172.32.5.1 
  (invalid, just past the upper edge) — the most common mistake when 
  hardcoding this range
- Known public IP (8.8.8.8) as a sanity check
- Malformed input: missing octet, extra octet, out-of-range octet 
  (999), non-numeric characters in different positions

## What I learned
- Never trust external input before validating its shape and range — 
  the classification logic only runs after the format check passes
- Most real bugs live at the boundaries of a valid range, not in the 
  middle of it
- Used `any()` with a generator expression for digit validation — 
  initially suggested by GitHub Copilot, then researched independently 
  until I could fully explain the logic myself

## Next challenge
Read the IP list from a file instead of manual input
