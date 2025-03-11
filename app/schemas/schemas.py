import datetime
from pydantic import BaseModel

class users(BaseModel): 
    userName: str
    email: str
    password: str

class taskType(BaseModel):
    typeName: str
    typeIdentifier: str
    
class taks(BaseModel):
    taskName: str
    taskDescription: str
    taskExpiration: datetime