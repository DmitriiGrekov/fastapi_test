from typing import List

from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from database import SessionLocal, engine

router = APIRouter()

from expenses.models import expenses

from expenses.schemas.expenses import ExpenseSchema
from expenses.schemas.expenses import ExpenseCreateSchema

from expenses.services.expenses import get_expense_by_user_id
from expenses.services.expenses import create_expense_by_user_id

from config.dependencies import get_db

expenses.Base.metadata.create_all(bind=engine)


@router.get('/{telegram_id}/')
async def get_user_expenses(telegram_id: int, db: Session = Depends(get_db)) -> List[ExpenseSchema]:
    """Получаем траты пользователя."""
    return await get_expense_by_user_id(telegram_id=telegram_id, db=db)

@router.post('/{telegram_id}/')
async def create_expenses(telegram_id: int, expense_data: ExpenseCreateSchema,  db: Session = Depends(get_db)) -> ExpenseSchema:
    """Создаем трату пользователя."""
    return await create_expense_by_user_id(telegram_id=telegram_id, expense_data=expense_data, db=db)
