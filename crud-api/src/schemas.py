from pydantic import BaseModel
from typing import Optional

class Product(BaseModel):
    id : int
    name : str
    price : float
    description : Optional[str] = None
    in_stock : bool
