import hashlib


def hash_password(password: str) -> str:
    """Hash a string to SHA256 as a secure password.

    Args:
        - password (str): unsecure password.

    Returns:
        - str: secure hashed password.

    """
    return hashlib.sha256(password.encode()).hexdigest()


def verify_password(password: str, hashed_password: str) -> bool:
    """Verify if the password is the same after hashing as the password hashed in the database.

    Args:
        - password (str): raw password.
        - hashed_password (str): password hashed.

    Returns:
        - bool: if the password is valid.
    """
    return hashed_password == hash_password(password)
