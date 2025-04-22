
from core.types.user_id import UserIDType
from fastapi_users import schemas


class UserRead(schemas.BaseUser[UserIDType]):
    pass


class UserCreate(schemas.BaseUserCreate):
    pass


class UserUpdate(schemas.BaseUserUpdate):
    pass