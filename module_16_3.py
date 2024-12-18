from fastapi import FastAPI, Path
from pydantic import BaseModel
from typing import Annotated


# Создаем экземпляр приложения FastAPI

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}

# Маршруты

@app.get("/users")
async def get_all_users():
    return users

@app.post("/user/{username}/{age}")
async def create_user(username: Annotated[str, Path(min_length=5, max_length=20,
                                      description="Enter username", example="UrbanUser")],
        age: Annotated[int, Path(ge=18, le=120, description="Enter age", example="24")]) -> str:
    user_id = str(int(max(users, key=int)) + 1)
    users[user_id] = f"Имя: {username}, возраст: {age}"
    resp=f"User {user_id} is registered"
    return resp

@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID", example="1")],
        username: Annotated[str, Path(min_length=5, max_length=20,
                                      description="Enter username", example="UrbanUser")],
        age: Annotated[int, Path(ge=18, le=120, description="Enter age", example="24")]):
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"The user {user_id} is updated"


@app.delete("/user/{user_id}")
async def delete_user(
        user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID", example="1")]):
    users.pop(str(user_id))
    return f"The user {user_id} is deleted"
    raise HTTPException(status_code=404, detail="User not found")



