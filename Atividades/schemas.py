from pydantic import BaseModel
from typing import Optional

class GodBase(BaseModel):
    name: str
    nativename: str
    atribuition: str
    simbols: str
    household: str
    foto: str

class GodCreate(GodBase):
    pass

class GodUpdate(BaseModel):
    name: Optional[str]
    nativename: Optional[str]
    atribuition: Optional[str]
    simbols: Optional[str]
    household: Optional[str]
    foto: Optional[str]

class GodOut(GodBase):
    id: int

    class Config:
        orm_mode = True
