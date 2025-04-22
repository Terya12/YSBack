from core.types.user_id import UserIDType
from fastapi_users import FastAPIUsers

from core.models.user import User
from api.dependencies.authentication.backend import authentication_backends
from api.dependencies.authentication.user_manager import get_user_manager

fastapi_users = FastAPIUsers[User, UserIDType](
    get_user_manager,
    [authentication_backends],
)


current_user = fastapi_users.current_user(active=True)
current_super_user = fastapi_users.current_user(superuser=True)