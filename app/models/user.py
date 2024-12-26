from sqlalchemy import Column, Integer, String
from app.db.base_class import Base


class User(Base):
    __tablename__ = "uf_users"

    id = Column(Integer, autoincrement=True, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String,unique=True)
    