from crypto_utils import generate_salt, derive_key, encrypt_data, decrypt_data

salt = generate_salt()
key = derive_key("my_master_password", salt)

secret = b"my_super_secret_password"
encrypted = encrypt_data(secret, key)
print("Encrypted:", encrypted)

decrypted = decrypt_data(encrypted, key)
print("Decrypted:", decrypted)