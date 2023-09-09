from fastapi import APIRouter, Depends
from app.user.usecases import (create_user as _create_user,
                               get_user as _get_user,
                               delete_user as _delete_user,
                               get_all_users as _get_all_users)
from app.user.dtos import ReadUserDto, WriteUserDto
from server.dependencies import get_user_repo
from app.user.interfaces import UserRepository

router = APIRouter()


@router.post('/')
async def create_user(user: WriteUserDto,
                      user_repo: UserRepository = Depends(get_user_repo)):
    await _create_user(user, user_repo)


@router.get('/{id}')
async def get_user(id: int,
                   user_repo: UserRepository = Depends(get_user_repo)
                   ) -> ReadUserDto:
    return await _get_user(id, user_repo)


@router.delete('/{id}')
async def delete_user(id: int,
                      user_repo: UserRepository = Depends(get_user_repo)):
    await _delete_user(id, user_repo)


@router.get('/')
async def get_all_users(user_repo: UserRepository = Depends(get_user_repo)
                        ) -> list[ReadUserDto]:
    return await _get_all_users(user_repo)
