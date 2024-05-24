from sqlalchemy import Column, Integer, String, Double, Date

from ...database import Base


class DevModel(Base):
    __tablename__ = "dev"

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    birth_date = Column(Date)
    salary = Column(Double)