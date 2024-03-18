from fastapi import HTTPException
from sqlalchemy.orm import Session

from expenses.models.expenses import ExpenseModel

from expenses.schemas.expenses import ExpenseCreateSchema
from expenses.schemas.expenses import ExpenseSchema



from users.schemas.user import UserCreate
from users.schemas.user import User
from users.models.user import UserModel


async def get_expense_by_user_id(telegram_id: int, db: Session):
    """Получаем затраты пользователя по telegram_id пользователя."""
    return db.query(ExpenseModel).filter(ExpenseModel.user_id == telegram_id).all()


async def create_expense_by_user_id(telegram_id: int, expense_data: ExpenseCreateSchema, db: Session) -> ExpenseSchema:
    """Создаем трату пользователя."""
    expense = ExpenseModel(**expense_data.model_dump(), user_id=telegram_id)
    db.add(expense)
    db.commit()
    db.refresh(expense)
    return expense