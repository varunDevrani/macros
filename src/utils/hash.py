from argon2 import PasswordHasher
from argon2.exceptions import (
    VerifyMismatchError,
    VerificationError,
    InvalidHashError
)

passwordHasher = PasswordHasher()


def hash_password(
    plain_password: str
) -> str:
    return passwordHasher.hash(plain_password)
    
    
def verify_password(
    plain_password: str,
    hashed_password: str
) -> bool:
    try:
        passwordHasher.verify(hashed_password, plain_password)
        return True
    except VerifyMismatchError or VerificationError or InvalidHashError:
        return False

