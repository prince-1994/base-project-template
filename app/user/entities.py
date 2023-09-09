from pydantic import BaseModel


class User(BaseModel):
    id: int | None
    first_name: str
    last_name: str
    age: int
