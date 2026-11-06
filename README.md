# Data Sanitizer

A Python project containing data-sanitization logic in `sanitizer.py`.

## Requirements
- Python 3.8 or later

## Run
```bash
git clone https://github.com/dperry713/data_sanitizer.git
cd data_sanitizer
python sanitizer.py
```

If the module is designed for reuse, import its sanitization functions into the calling application.

## Project structure
- `sanitizer.py` — data-sanitization implementation.

## Development and security
Define supported inputs and output formats. Prefer context-specific encoding and validation over indiscriminate character removal. Test malformed input, Unicode, empty values, and security-sensitive edge cases.