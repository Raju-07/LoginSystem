from sqlalchemy.orm import DeclarativeBase,mapped_column,Mapped
from sqlalchemy import Integer,UUID,String,Boolean,func,text,DateTime
from sqlalchemy import Enum as SQLEnum
import uuid
from datetime import datetime,timedelta,timezone
from enum import Enum

class Base(DeclarativeBase):
    pass

# ROles of USER THROUGH Custom DataTYPE
class Role(str,Enum):
    USERADMIN = "super_admin"
    ADMIN = "admin"
    SUPERVISOR = "supervisor"
    TEAM_LEAD = "team_lead"
    USER = "user"

# SIGN UP MODAL
class UserRegisterModal(Base):

    __tablename__ = "users"

    id : Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        default=lambda : uuid.uuid4(),
        server_default=text("gen_random_uuid()"),
        primary_key=True,
        index=True)
    
    name : Mapped[str] = mapped_column(
        String(100),
        nullable=False)
    
    username : Mapped[str] = mapped_column(
        String(200),
        unique=True,
        nullable=False)
    
    email : Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False)
    
    password : Mapped[str] = mapped_column(
        String,
        nullable=False)
    
    role : Mapped[Role] = mapped_column(
        SQLEnum(Role,native_enum=False),
        nullable=False,
        default=Role.USER.value
        )
    
    is_active : Mapped[bool] = mapped_column(
        Boolean,default=True,
        nullable=False)
    
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        server_default=func.current_timestamp(),
        nullable=False)
    # Enabling ORM
    class Config:
        from_attributes = True
