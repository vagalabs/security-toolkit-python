import json
import os
from crypto_utils import generate_salt, derive_key, encrypt_data, decrypt_data

VAULT_FILE = "vault.dat"
SALT_FILE = "salt.bin"


def vault_exists() -> bool:
    return os.path.exists(VAULT_FILE) and os.path.exists(SALT_FILE)


def create_vault(master_password: str) -> bytes:
    """Create a new empty vault, encrypted with the master password."""
    salt = generate_salt()
    with open(SALT_FILE, "wb") as f:
        f.write(salt)

    key = derive_key(master_password, salt)
    empty_data = json.dumps({}).encode()
    encrypted = encrypt_data(empty_data, key)

    with open(VAULT_FILE, "wb") as f:
        f.write(encrypted)

    return key


def load_vault(master_password: str) -> tuple[dict, bytes]:
    """Load and decrypt the vault. Raises an exception if the password is wrong."""
    with open(SALT_FILE, "rb") as f:
        salt = f.read()

    key = derive_key(master_password, salt)

    with open(VAULT_FILE, "rb") as f:
        encrypted = f.read()

    decrypted = decrypt_data(encrypted, key)
    data = json.loads(decrypted.decode())
    return data, key


def save_vault(data: dict, key: bytes) -> None:
    """Encrypt and save the vault data back to disk."""
    encoded = json.dumps(data).encode()
    encrypted = encrypt_data(encoded, key)
    with open(VAULT_FILE, "wb") as f:
        f.write(encrypted)