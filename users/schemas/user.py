from typing import Union, List

from pydantic import BaseModel

from expenses.schemas.expenses import ExpenseSchema


class UserBase(BaseModel):
    """Базовая схема пользователя."""
    username: Union[str, None] = None
    telegram_id: int
    is_active: bool = True


class UserCreate(UserBase):
    """Схема для создания пользователя."""
    ...


class User(UserBase):
    """Полная схема пользователя"""
    id: int

    expenses: List[ExpenseSchema]

    class Config:
        from_attributes = True



