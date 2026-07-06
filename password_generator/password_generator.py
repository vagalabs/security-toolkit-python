import secrets
import string
import argparse


def generate_password(length: int, use_letters: bool, use_digits: bool, use_symbols: bool) -> str:
    """
    Generate a secure random password based on selected character sets.
    """

    if length <= 0:
        raise ValueError("Password length must be greater than 0")

    characters = ""

    if use_letters:
        characters += string.ascii_letters

    if use_digits:
        characters += string.digits

    if use_symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character set must be selected")

    password = "".join(secrets.choice(characters) for _ in range(length))
    return password


def main():
    parser = argparse.ArgumentParser(description="Secure Password Generator")

    parser.add_argument("-l", "--length", type=int, default=12, help="Password length")
    parser.add_argument("--no-letters", action="store_true", help="Exclude letters")
    parser.add_argument("--no-digits", action="store_true", help="Exclude digits")
    parser.add_argument("--no-symbols", action="store_true", help="Exclude symbols")

    args = parser.parse_args()

    password = generate_password(
        length=args.length,
        use_letters=not args.no_letters,
        use_digits=not args.no_digits,
        use_symbols=not args.no_symbols
    )

    print("\nGenerated Password:")
    print(password)


if __name__ == "__main__":
    main()
