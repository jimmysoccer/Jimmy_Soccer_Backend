from sqlalchemy import Column, Integer, String, Float, Date

from ...database import Base


class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password  = Column(String)
