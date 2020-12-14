from pydantic import BaseModel
from datetime import datetime

class TransactionIn(BaseModel):
    username: str
    cuenta: str
    income: int
    expense: int

class TransactionOut(BaseModel):
    id_transaction: int
    username: str
    cuenta: str
    date: datetime
    income: int
    expense: int
    actual_balance: int