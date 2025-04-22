import logging
import re
from typing import Optional

from fastapi import Request
from fastapi_users import BaseUserManager, IntegerIDMixin, InvalidPasswordException
from core.config import settings
from core.types.user_id import UserIDType
from core.models.user import User


log = logging.getLogger(__name__)


class UserManager(IntegerIDMixin, BaseUserManager[User, UserIDType]):
    reset_password_token_secret = settings.access_token.reset_password_token_secret
    verification_token_secret = settings.access_token.verification_token_secret

    async def on_after_register(
        self,
        user: User,
        request: Optional[Request] = None,
    ):
        log.warning(
            "User %s has registered.",
            user.id,
        )

    async def on_after_request_verify(
        self,
        user: User,
        token: str,
        request: Optional[Request] = None,
    ):
        log.warning(
            "Verification requested for user %s. Verification token: %s",
            user.id,
            token,
        )
    async def on_after_forgot_password(
        self,
        user: User,
        token: str,
        request: Optional[Request] = None,
    ):
        log.warning(
            "User %s has forgot their password. Reset token: %s",
            user.id,
            token,
        )

    # async def validate_password(
    #     self,
    #     password: str,
    #     user: Optional[User] = None,
    # ) -> None:
    #     # Проверка минимальной длины пароля
    #     if len(password) < 8:
    #         raise InvalidPasswordException(
    #             reason="Password should be at least 8 characters"
    #         )

    #     # Проверка на наличие хотя бы одной цифры
    #     if not re.search(r'\d', password):
    #         raise InvalidPasswordException(
    #             reason="Password should contain at least one digit"
    #         )

    #     # Проверка на наличие хотя бы одного специального символа
    #     if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
    #         raise InvalidPasswordException(
    #             reason="Password should contain at least one special character"
    #         )

    #     # Проверка на наличие хотя бы одной буквы в верхнем и одном в нижнем регистре
    #     if not re.search(r'[A-Z]', password):
    #         raise InvalidPasswordException(
    #             reason="Password should contain at least one uppercase letter"
    #         )
    #     if not re.search(r'[a-z]', password):
    #         raise InvalidPasswordException(
    #             reason="Password should contain at least one lowercase letter"
    #         )

    #     # Проверка на отсутствие простых последовательностей
    #     if re.search(r'(1234|abcd|password)', password):
    #         raise InvalidPasswordException(
    #             reason="Password should not contain simple sequences like '1234' or 'abcd'"
    #         )

    #     # Проверка на отсутствие повторяющихся символов
    #     if re.search(r'(.)\1{2,}', password):  # 3 одинаковых символа подряд
    #         raise InvalidPasswordException(
    #             reason="Password should not contain repeated characters like 'aaa'"
    #         )