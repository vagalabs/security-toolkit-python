import getpass
from vault import vault_exists, create_vault, load_vault, save_vault
import secrets
import string


def generate_password(length: int = 16) -> str:
    """Generate a secure random password."""
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return "".join(secrets.choice(alphabet) for _ in range(length))


def print_menu():
    print("\n=== Password Manager ===")
    print("1. Add entry")
    print("2. View entry")
    print("3. List all sites")
    print("4. Delete entry")
    print("5. Exit")


def add_entry(data: dict):
    site = input("Site/service name: ").strip()
    username = input("Username/email: ").strip()

    choice = input("Generate a secure password automatically? (y/n): ").strip().lower()
    if choice == "y":
        length_input = input("Password length (default 16): ").strip()
        length = int(length_input) if length_input.isdigit() else 16
        password = generate_password(length)
        print(f"Generated password: {password}")
    else:
        password = getpass.getpass("Password: ")

    data[site] = {"username": username, "password": password}
    print(f"Entry for '{site}' added.")


def view_entry(data: dict):
    site = input("Site/service name: ").strip()
    entry = data.get(site)
    if entry:
        print(f"Username: {entry['username']}")
        print(f"Password: {entry['password']}")
    else:
        print("No entry found for that site.")


def list_sites(data: dict):
    if not data:
        print("Vault is empty.")
    else:
        print("Stored sites:")
        for site in data:
            print(f" - {site}")


def delete_entry(data: dict):
    site = input("Site/service name to delete: ").strip()
    if site in data:
        del data[site]
        print(f"Entry for '{site}' deleted.")
    else:
        print("No entry found for that site.")


def main():
    if not vault_exists():
        print("No vault found. Let's create one.")
        master_password = getpass.getpass("Set a master password: ")
        confirm = getpass.getpass("Confirm master password: ")
        if master_password != confirm:
            print("Passwords do not match. Exiting.")
            return
        key = create_vault(master_password)
        data = {}
        print("Vault created successfully.")
    else:
        master_password = getpass.getpass("Enter master password: ")
        try:
            data, key = load_vault(master_password)
        except Exception:
            print("Incorrect password or corrupted vault.")
            return

    while True:
        print_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_entry(data)
            save_vault(data, key)
        elif choice == "2":
            view_entry(data)
        elif choice == "3":
            list_sites(data)
        elif choice == "4":
            delete_entry(data)
            save_vault(data, key)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.")


if __name__ == "__main__":
    main()