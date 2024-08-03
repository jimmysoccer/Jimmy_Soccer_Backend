from sqlalchemy import Column, Integer, String, Date, Text
from datetime import datetime
from pydantic import BaseModel
from ...database import Base
from typing import Optional


class ProjectModel(BaseModel):
    id:Optional[int] = None
    title: str
    place: str
    start_date: datetime
    end_date: datetime
    description: str
    images: str


class Project(Base):
    __tablename__ = "projects"

    def __init__(self, title, place, start_date, end_date, description, images):
        self.title = title
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.images = images

    id = Column(Integer, primary_key=True)
    title = Column(String)
    place = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)
    description = Column(String)
    images = Column(String)
