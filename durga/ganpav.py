from fastapi import FastAPI
app = FastAPI()
@app.get("/") # @ is a decorator,/ is create url,
def read_root():
    return {"message": "Hello, FastAPI is working!"}

