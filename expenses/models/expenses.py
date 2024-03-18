import datetime

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship

from database import Base


class ExpenseModel(Base):
    """Модель трат пользователя."""

    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True)
    cost = Column(Float, default=0.0)
    created_at = Column(DateTime, default=datetime.datetime.now)
    description = Column(String, nullable=True)

    user_id = Column(Integer, ForeignKey('users.telegram_id'))

    user = relationship('UserModel', back_populates='expenses')


