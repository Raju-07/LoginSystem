from fastapi import APIRouter,Depends,HTTPException,status
from fastapi.security import OAuth2PasswordRequestForm
from app.core.security import hash_password,verify_password,create_session_token
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas import UserRegisterRequest
from app.db.session import get_async_db
from sqlalchemy import select,or_,insert
from app.models import UserRegisterModal
from app.core.security import hash_password

router = APIRouter(prefix="/auth")


# Create a USER

@router.post('/sign-up')
async def sign_up(
    new_user: UserRegisterRequest, db: AsyncSession = Depends(get_async_db)):

    # search for username & email if exists raise exception
    user_exists = await db.execute(
        select(UserRegisterModal).where(or_(
            UserRegisterModal.username == new_user.username,
            UserRegisterModal.email==new_user.email
            )
        )
    )

    user_found = user_exists.scalar_one_or_none()

    if user_found:
        if user_found.username == new_user.username:
            raise HTTPException(
            status.HTTP_409_CONFLICT,
            f"Username: {new_user.username} already exists"
            )
        else:
            raise HTTPException(
                status.HTTP_409_CONFLICT,
                f"Email: {new_user.email} already exists"
            )


    # No user Found -> Create New account

    #hashing plain password

    hashed_password = hash_password(new_user.password)

    #new_user creatation
    try:
        new_user_data = new_user.model_dump()
        new_user_data['password'] = hashed_password

        user = UserRegisterModal(**new_user_data)
        db.add(user)
        await db.commit()
        await db.refresh(user)

        return {
            'Code': 200,
            'Message':'New Account Created Sucessfully',
            'user Details': {
                'username':user
            }
        }
    
    except Exception as e:
        await db.rollback()
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST,
            f"Creation Failed.\n Error: {e}"
        )


# Login / Token endpoint
@router.post('/login')
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_async_db)
):
    query = await db.execute(
        select(UserRegisterModal).where(UserRegisterModal.username == form_data.username)
    )
    user = query.scalar_one_or_none()

    if not user:
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST,
            "Incorrect username or password"
        )

    if not verify_password(form_data.password, user.password):
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST,
            "Incorrect username or password"
        )

    token_payload = {"sub": str(user.id)}
    access_token = create_session_token(token_payload)

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }




