from typing import Optional
from pydantic import BaseModel

class Gods(BaseModel):
    id : Optional[int] = None
    name : str
    nativename : str
    atribuition : str
    simbols  : str
    household : str
    foto : str
    