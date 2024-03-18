from fastapi import HTTPException
from sqlalchemy.orm import Session

from users.schemas.user import UserCreate
from users.schemas.user import User
from users.models.user import UserModel


def _get_user_by_telegram_id(db: Session, telegram_id: int) -> User:
    users = db.query(UserModel).filter(UserModel.telegram_id == telegram_id).all()
    if not users:
        raise HTTPException(status_code=404, detail='Пользователь с данным telegram_id не найден')
    return users[0]


async def create_user(db: Session, user_data: UserCreate) -> UserModel:
    """Создание пользователя."""
    if db.query(UserModel).filter(UserModel.telegram_id == user_data.telegram_id).first():
        raise HTTPException(status_code=400, detail='Пользователь с данным telegram_id уже существует')
    
    user = UserModel(**user_data.model_dump())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


async def get_user_by_telegram_id(db: Session, telegram_id: int) -> User:
    """Получаем пользователя по telegram_id."""
    return _get_user_by_telegram_id(db, telegram_id)