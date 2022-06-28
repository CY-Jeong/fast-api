from typing import Union, Optional, List
from fastapi import FastAPI
from dtos.user_dto import UserDto, Gender
from fastapi import Depends, Query

app = FastAPI()


@app.get("/")
async def get_default_user(user: UserDto = Depends(UserDto)):
    return {"user": user}

@app.get("/{user_name}")
async def call_user(user_name):
    return {"user": user_name}

@app.post("/users/{check}")
async def call_user(user: UserDto, check: str = "cyj", gender: Optional[List[str]] = Query(max_length=2, deprecated=True, include_in_schema=False)):
    if (check == "cyj" or check == user.name):
        user_dict = user.dict()
        user_dict.update({"gender": gender})
        return {"user" : user_dict}
    else:
        return "I don't know"

@app.get("/users/{user}/{gender}")
async def check_gender(gender: Gender, user: str):
    if gender == Gender.male:
        return f"{user}'s gender is {gender.value}"
    elif gender == Gender.female:
        return f"{user}'s gender is {gender}"
    elif gender == Gender.trans:
        return f"{user}'s gender is {gender}"
    else:
        return f"{user} is lier"

@app.get("/files/{file_path:path}")
async def get_file_path(file_path: str):
    return file_path


@app.put("/users/{user_name}")
async def change_user_age(user: UserDto = Depends(UserDto)):
    return

