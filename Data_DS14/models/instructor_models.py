from core.configs import settings
from sqlalchemy import Column, Integer, Boolean, Float, String


class InstructorModel(settings.DBBaseModel):
    __tablename__ = "instructor"
    
    id: int = Column(Integer(), primary_key=True, autoincrement=True)
    name: str = Column(String(256))
    age: int = Column(Integer())
    subject : str = Column(String(256))
    photo: str = Column(String(2056))