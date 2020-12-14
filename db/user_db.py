from typing import Dict
from pydantic import BaseModel

class UserInDB(BaseModel):
    username: str
    password: str
    balance: int

database_users = Dict[str, UserInDB]
database_users = {
    "edwin182": UserInDB(**{"username":"edwin182",
                            "password":"123456qwert",
                            "balance":2033000}),
    "jhon1031": UserInDB(**{"username":"jhon1031",
                            "password":"uis2020",
                            "balance":4500000}),
    "rosa": UserInDB(**{"username":"rosa",
                            "password":"contraseña",
                            "balance":5000000}),
    "juan": UserInDB(**{"username":"juan",
                            "password":"juanito",
                            "balance":2890000}),
    "anderson": UserInDB(**{"username":"anderson",
                            "password":"agjapon",
                            "balance":3589400}),                       
}
def get_user(username: str):
    if username in database_users.keys():
        return database_users[username]
    else:
        return None
def update_user(user_in_db: UserInDB):
    database_users[user_in_db.username] = user_in_db
    return user_in_db