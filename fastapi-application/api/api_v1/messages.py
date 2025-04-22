from typing import Annotated
from fastapi import Depends
from fastapi import APIRouter
from core.models.user import User
from core.config import settings
from core.schemas.user import UserRead
from api.dependencies.authentication.fastapi_users import (
    current_user,
    current_super_user,
)


router = APIRouter(
    prefix=settings.api.v1.messages,
    tags=["Messages"],
)


@router.get("/")
def get_user_messages(
    user: Annotated[
        User,
        Depends(current_user),
    ],
):
    return {
        "messages": ["m1", "m2", "m3"],
        "user": UserRead.model_validate(user),
    }


@router.get("/secrets")
def get_super_user_messages(
        user: Annotated[
        User,
        Depends(current_super_user),
    ],
):
    return {
        "messages": ["secreat m1", "secreat m2", "secreat m3"],
        "user": UserRead.model_validate(user),
    }
