from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI from Ahsan Raza"}

@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello {name}"}

@app.get("/greet/{name}/{age}")
def greet(name: str, age: int):
    return {"message": f"Hello {name}, you are {age} years old"}

