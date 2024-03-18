from typing import Union

from datetime import datetime
from pydantic import BaseModel


class BaseExpenseSchema(BaseModel):
    """Базовая схема затрат пользователя."""
    cost: int
    description: Union[str, None] = None


class ExpenseCreateSchema(BaseExpenseSchema):
    """Схема создания затрат пользователя."""
    ...


class ExpenseSchema(BaseExpenseSchema):
    """Схема затрат пользователя."""
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
