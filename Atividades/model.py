from typing import Optional, Dict
from pydantic import BaseModel

class Gods(BaseModel):
    name : str
    nativename : str
    atribuition : str
    simbols  : str
    household : str
    foto : str

class Updates(BaseModel):
    name : Optional[str] = None
    nativename : Optional[str] = None
    atribuition : Optional[str] = None
    simbols  : Optional[str] = None
    household : Optional[str] = None
    foto : Optional[str] = None