from sqlalchemy import Column, Integer, String
from database import Base

class God(Base):
    __tablename__ = "gods"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    nativename = Column(String)
    atribuition = Column(String)
    simbols = Column(String)
    household = Column(String)
    foto = Column(String)
