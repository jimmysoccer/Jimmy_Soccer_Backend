from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from pydantic import BaseModel
from ...database import Base
from typing import Optional


class ContactModel(BaseModel):
    title: str
    content: str
    email: str


class ContactDBModel(Base):
    __tablename__ = "contact"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
    email = Column(String)
    sent_date = Column(DateTime)
