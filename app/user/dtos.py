from .entities import User
from pydantic import BaseModel


class ReadUserDto(User):
    first_name: str
    last_name: str
    age: int


class WriteUserDto(BaseModel):
    first_name: str
    last_name: str
    age: int
