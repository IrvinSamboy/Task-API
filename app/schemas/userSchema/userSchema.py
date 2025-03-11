from pydantic import BaseModel

class usersIn(BaseModel): 
    userName: str
    email: str
    password: str

class userOut(BaseModel):
    userName: str
    email: str
