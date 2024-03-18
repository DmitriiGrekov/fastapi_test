from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from database import SessionLocal, engine

router = APIRouter()

from users.models import user
from users.schemas.user import UserCreate
from users.schemas.user import User
from users.services.users import create_user
from users.services.users import get_user_by_telegram_id

from config.dependencies import get_db

user.Base.metadata.create_all(bind=engine)


@router.post('/')
async def create_user_view(user_dto: UserCreate, db: Session = Depends(get_db)) -> User:
    return await create_user(db, user_dto)


@router.get('/{telegram_id}/')
async def get_user_by_telegram_id_view(telegram_id: int, db: Session = Depends(get_db)) -> User:
    return await get_user_by_telegram_id(db, telegram_id)