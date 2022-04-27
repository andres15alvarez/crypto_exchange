import hashlib


def hash_password(password: str) -> str:
    """Hash a string to SHA256 as a secure password.

    Args:
        - password (str): unsecure password.

    Returns:
        - str: secure hashed password.

    """
    return hashlib.sha256(password.encode()).hexdigest()