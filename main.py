from fastapi import FastAPI, Request, Depends
from starlette import status
import models
from database import engine
from routers import auth, todos, users
from starlette.staticfiles import StaticFiles
from fastapi import FastAPI
from routers.auth import get_current_user

from starlette.responses import RedirectResponse

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def root_redirect():
    return RedirectResponse(url="/todos", status_code=status.HTTP_302_FOUND)


app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(users.router)
