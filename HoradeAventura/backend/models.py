from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Reino(Base):
    __tablename__ = "reinos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, unique=True, index=True)
    personagens = relationship("Personagem", back_populates="reino")

class Personagem(Base):
    __tablename__ = "personagens"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    tipo = Column(String)
    reino_id = Column(Integer, ForeignKey("reinos.id"))

    reino = relationship("Reino", back_populates="personagens")
