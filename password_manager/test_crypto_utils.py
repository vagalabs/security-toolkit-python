import pytest
from crypto_utils import generate_salt, derive_key, encrypt_data, decrypt_data


def test_generate_salt_length():
    """Salt should be 16 bytes long."""
    salt = generate_salt()
    assert len(salt) == 16


def test_generate_salt_is_random():
    """Two generated salts should not be identical."""
    salt1 = generate_salt()
    salt2 = generate_salt()
    assert salt1 != salt2


def test_derive_key_same_password_and_salt_gives_same_key():
    """Deriving a key twice with the same password and salt should be deterministic."""
    salt = generate_salt()
    key1 = derive_key("my_password", salt)
    key2 = derive_key("my_password", salt)
    assert key1 == key2


def test_derive_key_different_passwords_give_different_keys():
    """Different passwords should produce different keys even with the same salt."""
    salt = generate_salt()
    key1 = derive_key("password_one", salt)
    key2 = derive_key("password_two", salt)
    assert key1 != key2


def test_derive_key_different_salts_give_different_keys():
    """The same password with different salts should produce different keys."""
    key1 = derive_key("same_password", generate_salt())
    key2 = derive_key("same_password", generate_salt())
    assert key1 != key2


def test_encrypt_decrypt_round_trip():
    """Encrypting then decrypting should return the original data."""
    salt = generate_salt()
    key = derive_key("test_password", salt)

    original = b"my secret password"
    encrypted = encrypt_data(original, key)
    decrypted = decrypt_data(encrypted, key)

    assert decrypted == original


def test_encrypted_data_is_not_plaintext():
    """Encrypted data should not contain the original plaintext."""
    salt = generate_salt()
    key = derive_key("test_password", salt)

    original = b"super_secret_value"
    encrypted = encrypt_data(original, key)

    assert original not in encrypted


def test_decrypt_with_wrong_key_fails():
    """Decrypting with the wrong key should raise an exception."""
    salt = generate_salt()
    correct_key = derive_key("correct_password", salt)
    wrong_key = derive_key("wrong_password", salt)

    encrypted = encrypt_data(b"secret data", correct_key)

    with pytest.raises(Exception):
        decrypt_data(encrypted, wrong_key)