from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError,InvalidHashError
from app.core.config import settings
from datetime import datetime,timedelta,timezone
import jwt

#instanciating 
pwd_hasher = PasswordHasher()


def hash_password(password:str) -> str:
    return pwd_hasher.hash(password)


def verify_password(password: str,hash:str) -> bool:
    try:
        pwd_hasher.verify(hash,password)
        return True
    except (VerifyMismatchError,InvalidHashError):
        return False

def create_session_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes = settings.token_expire)
    to_encode.update({'exp':expire})
    return jwt.encode(to_encode,settings.secret_key,settings.algorithm)



