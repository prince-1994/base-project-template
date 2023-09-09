from fastapi import FastAPI
from server.endpoints.user import router as users_router
from server.dependencies import get_settings, get_database

app = FastAPI(debug=get_settings().debug)


@app.on_event('startup')
async def startup():
    await get_database().connect()


@app.on_event('shutdown')
async def shutdown():
    await get_database().disconnect()

app.include_router(users_router, prefix='/users')
