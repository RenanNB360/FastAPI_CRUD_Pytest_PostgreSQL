from fastapi import FastAPI, status

from fast_postgres.routers import auth, users
from fast_postgres.schema import (
    Message,
)

app = FastAPI()

app.include_router(users.router)
app.include_router(auth.router)


@app.get('/', status_code=status.HTTP_200_OK, response_model=Message)
async def read_root():
    return {'message': 'Olá Mundo!'}
