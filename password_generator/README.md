# Password Generator

## Description
A secure CLI tool for generating random passwords using Python.

## Features
- Custom password length
- Option to include/exclude letters
- Option to include/exclude digits
- Option to include/exclude symbols
- Uses `secrets` module (cryptographically secure)

## Usage

```bash
python password_generator.py -l 16
```

### Without symbols:
```bash
python password_generator.py -l 16 --no-symbols
```

## Security Note
This tool uses Python's `secrets` module instead of `random` for cryptographic security.
