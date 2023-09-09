from .entities import User
from .dtos import ReadUserDto, WriteUserDto
from .interfaces import UserRepository


async def get_user(id: int, user_repo: UserRepository) -> ReadUserDto:
    user = await user_repo.find_one(id)
    return ReadUserDto(**user.dict())


async def get_all_users(user_repo: UserRepository) -> ReadUserDto:
    users = await user_repo.find_all()
    return [ReadUserDto(**user.dict()) for user in users]


async def create_user(user: WriteUserDto, user_repo: UserRepository):
    user = await user_repo.create(User(**user.dict()))


async def delete_user(id: int, user_repo: UserRepository):
    await user_repo.delete(id)
