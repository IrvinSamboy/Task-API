import datetime
from pydantic import BaseModel


class taskType(BaseModel):
    typeName: str
    typeIdentifier: str

class taks(BaseModel):
    taskName: str
    taskDescription: str
    taskExpiration: datetime
