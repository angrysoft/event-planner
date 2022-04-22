from django.conf import settings
from django.contrib.auth.backends import BaseBackend
from user_auth.models import User, Token
from django.http import HttpRequest
import jwt


class TokenBackend(BaseBackend):
    def authenticate(self, request: HttpRequest) -> User | None:
        try:
            token = request.headers.get("token")
            print("auth", token)
            payload = jwt.decode(token, settings.JWTKEY, algorithms=["HS256"])
            if not Token.objects.filter(token__exact=payload.get("token")).exists():
                print("debug: token not found")
                return None
            user = User.objects.get(username=payload.get("username", ""))
            return user
        except jwt.exceptions.InvalidTokenError:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
