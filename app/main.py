from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def server_runing():
    return {"Hello" : "World"}