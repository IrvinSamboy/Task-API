from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import column, Integer, String, DateTime

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
    typeNAme = column(String, nulleable=False)
    typeIdentifier = column(String, nulleable=False)

class tasks(Base):
    idTask = column(Integer, primary_key=True)
    taskName = column(String, nulleable=False)
    taskDescription = column(String, nulleable=False)
    taskExpiration = column(DateTime, nulleable=True)