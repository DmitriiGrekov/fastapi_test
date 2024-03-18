from fastapi import Depends, FastAPI, HTTPException
from fastapi import FastAPI

from sqlalchemy.orm import Session

from database import SessionLocal, engine

from users.views.users import router as UserRouter
from expenses.views.expenses import router as ExpenseRouter

from config import settings

app = FastAPI()


app.include_router(UserRouter, prefix=f'{settings.URL_PREFIX}/users')
app.include_router(ExpenseRouter, prefix=f'{settings.URL_PREFIX}/expense')
