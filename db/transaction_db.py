from datetime import datetime
from pydantic import BaseModel

class TransactionInDB(BaseModel):
    id_transaction: int = 0
    username: str
    descripcion: str
    date: datetime = datetime.now()
    ingreso: int
    egreso: int
    actual_balance: int

database_transactions = []
generator = {"id":0}

def save_transaction(transaction_in_db: TransactionInDB):
    generator["id"] = generator["id"] + 1
    transaction_in_db.id_transaction = generator["id"]
    database_transactions.append(transaction_in_db)
    return transaction_in_db

def get_transactions(username: str):
    transactions = []
    for t in database_transactions:
        if t.username == username:
            transactions.append(t)
    return transactions

