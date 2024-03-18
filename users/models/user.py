from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class UserModel(Base):
    """Класс модели пользователя."""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=True)
    telegram_id = Column(Integer, unique=True, index=True)
    is_active = Column(Boolean, default=True)

    expenses = relationship('ExpenseModel', back_populates='user')