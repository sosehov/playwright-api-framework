from pydantic import BaseModel


class UserSchema(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str


class GetUserResponse(BaseModel):
    data: UserSchema
    support: dict


class CreateUserResponse(BaseModel):
    name: str
    job: str
    id: str
    createdAt: str


class UpdateUserResponse(BaseModel):
    name: str
    job: str
    updatedAt: str
