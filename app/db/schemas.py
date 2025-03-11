from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import column, Integer, String

Base = declarative_base()

class users(Base): 
    __tablename__ = "users"

    idUSer = column(Integer, primary_key=True)
    userName = column(String, nulleable=False)
    email= column(String, nulleable=False)
    password= column(String, nulleable=False)

class taskType(Base):
    __tableNAme__ = "taskType"

    idTask = column(Integer, primary_key=True)
    taskNAme = column(String, nulleable=False)
    typeIdentifier = column(String, nulleable=False)

