from fastapi import FastAPI
from pydantic import BaseModel

# 1. Create FastAPI app
app = FastAPI()

# 2. Define data model
class User(BaseModel):
    id: int
    name: str
    age: int

# 3. POST API
@app.post("/users/")
def create_user(user: User):
    return {"message": "User created", "user": user}

