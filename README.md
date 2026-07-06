# Password Manager

A secure command-line password manager built in Python, using industry-standard encryption practices.

## Features
- Master password protects access to all stored credentials
- Encryption via Fernet (AES-128) from the `cryptography` library
- Master password never stored — a key is derived using PBKDF2-HMAC-SHA256 (390,000 iterations)
- Add, view, list, and delete stored entries
- Built-in secure password generator (uses Python's `secrets` module)

## How it works
1. On first run, you set a master password. A random salt is generated and stored alongside the encrypted vault.
2. Your master password + salt are used to derive an encryption key (the password itself is never saved).
3. All entries (site, username, password) are stored in a single JSON blob, encrypted with that key.
4. On future runs, you re-enter the master password to decrypt and access your vault.

## Setup
```bash
pip install cryptography
python main.py
```

## Security notes
This project is built for learning purposes and demonstrates secure password storage practices (key derivation, salting, symmetric encryption). It is not intended for storing high-value production credentials — for that, use a well-audited tool like Bitwarden or KeePass.

## Tech stack
- Python 3
- `cryptography` (Fernet, PBKDF2HMAC)
- `secrets`, `getpass`, `json` (standard library)
## Testing
Unit tests cover the core encryption module (key derivation, encryption/decryption, wrong-password handling).

```bash
pip install pytest
python -m pytest -v
```