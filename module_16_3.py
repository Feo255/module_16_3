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
async def create_user(username: str, age: int) -> str:
    user_id = str(int(max(users, key=int)) + 1)
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return {f"User {user_id} is registered"}

@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: int, username: str, age: int):
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return {f"The user {user_id} is updated"}


@app.delete("/user/{user_id}")
async def delete_user(user_id: str):
    users.pop(user_id)
    return {f"The user {user_id} is deleted"}
    raise HTTPException(status_code=404, detail="User not found")



