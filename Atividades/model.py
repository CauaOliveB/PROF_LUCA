from typing import Optional, Dict
from pydantic import BaseModel

class Gods(BaseModel):
    name : str
    nativename : str
    atribuition : str
    simbols  : str
    household : str
    foto : str
    