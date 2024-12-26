from pydantic import BaseModel

class UserBase(BaseModel):
    email: str
    full_name: str = None
    mobile: str = None

class UserCreate(UserBase):
    hashed_password: str

class UserUpdate(UserBase):
    pass

class User(UserBase):
    id: int

    class Config:
        orm_mode = True