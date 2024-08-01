from sqlalchemy import Column, Integer, String, Float, Date

from ...database import Base


class DevModel(Base):
    __tablename__ = "dev"

    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname  = Column(String)
    birthdate  = Column(Date)
    salary = Column(Float)
