import sys

sys.path.append("..")
from starlette import status
from starlette.responses import RedirectResponse
from fastapi import Depends, APIRouter, Request, Form
from pydantic import BaseModel
from typing import Optional
import models
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from .auth import get_current_user, verify_password, get_password_hash

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


router = APIRouter(
    prefix="/users", tags=["users"], responses={404: {"description": "Not founf"}}
)

templates = Jinja2Templates(directory="templates")
models.Base.metadata.create_all(bind=engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


class UserVerification(BaseModel):
    username: str
    password: str
    new_password: str


@router.get("/edit-user", response_class=HTMLResponse)
async def edit_user_view(request: Request):
    user = await get_current_user(request)
    if user is None:
        return RedirectResponse(url="/auth", status_code=status.HTTP_302_FOUND)
    return templates.TemplateResponse(
        "edit-user-page.html", {"request": request, "user": user}
    )


@router.post("/edit-user", response_class=HTMLResponse)
async def update_user(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
    password2: str = Form(...),
    db: Session = Depends(get_db),
):

    user = await get_current_user(request)
    if user is None:
        return RedirectResponse(url="/auth", status_code=status.HTTP_302_FOUND)

    user_model = (
        db.query(models.Users).filter(models.Users.username == username).first()
    )
    msg = "Invalid username and password"
    if user_model is not None:
        if user_model.username == username and verify_password(
            password, user_model.hashed_password
        ):
            user_model.hashed_password = get_password_hash(password2)
            db.add(user_model)
            db.commit()
            msg = "User successfully updated"
    return templates.TemplateResponse(
        "edit-user-page.html", {"request": request, "msg": msg, "user": user}
    )
