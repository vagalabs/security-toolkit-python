import base64
import os
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet


def generate_salt() -> bytes:
    """Generate a random 16-byte salt."""
    return os.urandom(16)


def derive_key(password: str, salt: bytes) -> bytes:
    """Derive a 32-byte encryption key from the master password and salt."""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=390000,
    )
    key = kdf.derive(password.encode())
    return base64.urlsafe_b64encode(key)


def encrypt_data(data: bytes, key: bytes) -> bytes:
    """Encrypt raw bytes using the given key."""
    f = Fernet(key)
    return f.encrypt(data)


def decrypt_data(token: bytes, key: bytes) -> bytes:
    """Decrypt bytes previously encrypted with encrypt_data."""
    f = Fernet(key)
    return f.decrypt(token)