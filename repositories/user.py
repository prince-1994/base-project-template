from app.user.entities import User
from app.user.interfaces import UserRepository \
    as UserRepositoryInterface
from databases import Database
from database.tables import users
from sqlalchemy import select


class UserRepository(UserRepositoryInterface):
    def __init__(self, database: Database) -> None:
        self.database = database

    async def create(self, user: User) -> str | None:
        query = users.insert(user.dict(exclude_none=True))
        await self.database.execute(query)

    async def find_one(self, id: int) -> User:
        columns = [users.c.id,
                   users.c.first_name,
                   users.c.last_name,
                   users.c.age]
        query = select(columns).where(users.c.id == id)
        user_info = await self.database.fetch_one(query)
        return User(id=user_info[0],
                    first_name=user_info[1],
                    last_name=user_info[2],
                    age=user_info[3])

    async def delete(self, id: int):
        query = users.delete(users.c.id == id)
        await self.database.fetch_one(query)

    async def find_all(self) -> list[User]:
        query = users.select()
        results = await self.database.fetch_all(query)
        return [User(id=user_info[0],
                     first_name=user_info[1],
                     last_name=user_info[2],
                     age=user_info[3]) for user_info in results]
