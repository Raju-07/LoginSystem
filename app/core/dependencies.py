from fastapi import Depends,status,HTTPException
from app.schemas import UserDataResponse
from app.models import UserRegisterModal
from fastapi.security import OAuth2PasswordBearer
from app.db.session import get_async_db
from sqlalchemy.ext.asyncio import AsyncSession
import jwt
from app.core.config import settings
import uuid 
from sqlalchemy import select

oauth = OAuth2PasswordBearer(tokenUrl="/api/auth/login")

async def get_current_user(token: str = Depends(oauth),
                    db: AsyncSession = Depends(get_async_db)) -> UserDataResponse:

    credential_exception = HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        detail= "Could not valid credentials",
        headers={'WWW-AUTHENTICATE':'bearer'}
        )

    try:
        payload = jwt.decode(token,settings.secret_key,settings.algorithm)
        user_id = payload.get('sub')
        if not user_id:
            raise credential_exception

        # Handing jwt EXCEPTIONS

    except jwt.ExpiredSignatureError:
            raise credential_exception

    except jwt.PyJWTError:
            raise credential_exception

    # CONVERTING user_id : str -> user_id: uuid
    try:
        user_id = uuid.UUID(user_id)
    except ValueError:
        raise credential_exception

    # FETCHING COMPLETE USER DETAILS

    query = await db.execute(
        select(UserRegisterModal).where(UserRegisterModal.id == user_id))
    user = query.scalar_one_or_none()

    if not user or not user.is_active:
        raise credential_exception

    return user
            
async def admin_required(
        user: UserRegisterModal = Depends(get_current_user)):
    if user.role != 'admin':
        raise HTTPException(
            status.HTTP_403_FORBIDDEN,
            "Admin Previleges Required"
        )