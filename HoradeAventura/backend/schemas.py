from pydantic import BaseModel

class ReinoBase(BaseModel):
    nome: str

class ReinoCreate(ReinoBase):
    pass

class Reino(ReinoBase):
    id: int
    class Config:
        orm_mode = True

class PersonagemBase(BaseModel):
    nome: str
    tipo: str
    reino_id: int

class PersonagemCreate(PersonagemBase):
    pass

class Personagem(PersonagemBase):
    id: int
    class Config:
        orm_mode = True
