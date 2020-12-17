from pydantic import BaseModel
from datetime import datetime

class TransactionIn(BaseModel):
    username: str
    cuenta: str
    income: int
    expense: int

class TransactionOut(BaseModel):
    id_transaccion: int
    usuario: str
    cuenta: str
    fecha: datetime
    ingreso: int
    egreso: int
    balance: int