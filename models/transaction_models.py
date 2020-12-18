from pydantic import BaseModel
from datetime import datetime

class TransactionIn(BaseModel):
    username: str
    descripcion: str
    ingreso: int
    egreso: int

class TransactionOut(BaseModel):
    id_transaction: int
    username: str
    descripcion: str
    date: datetime
    ingreso: int
    egreso: int
    actual_balance: int