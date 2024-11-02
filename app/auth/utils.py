from bcrypt import hashpw, gensalt, checkpw

def hash_password(password):
    """Hash a password for storing."""
    salt = gensalt()
    hashed = hashpw(password.encode('utf-8'), salt)
    return hashed

def verify_password(password, hashed):
    """Verify a stored password against a provided password."""
    return checkpw(password.encode('utf-8'), hashed)