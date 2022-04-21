import uuid
from typing import Any, Dict
from django.http import HttpRequest, JsonResponse
from django.views import View
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import AbstractBaseUser
from django.conf import settings
import jwt

from user_auth.models import Token
from .forms import LoginForm


class LoginView(View):
    # @method_decorator(csrf_exempt)
    def post(self, request: HttpRequest):
        login_form = LoginForm(request.POST)
        results: Dict[str, Any] = {"result": {}}
        if login_form.is_valid():
            user = authenticate(
                request,
                username=login_form.cleaned_data.get("login"),
                password=login_form.cleaned_data.get("password"),
            )
            if user is not None:
                token = str(uuid.uuid4())
                results["result"]["token"] = self._generate_auth_jwt(user, token)
                self._save_token(user, token)
                login(request, user)
        else:
            results["error"] = login_form.errors.as_json()

        return JsonResponse(results)

    def _generate_auth_jwt(self, user: AbstractBaseUser, token: str) -> str:
        token: str = jwt.encode(
            {"user": user.username, "token": token},
            settings.JWTKEY,
            algorithm="HS256",
        )
        print(type(token))
        return token

    def _save_token(self, user: AbstractBaseUser, token: str):
        Token.objects.filter(user__exact=user).delete()
        token_obj = Token()
        token_obj.user = user
        token_obj.token = token
        token_obj.save()


def logoutView(request: HttpRequest):
    print(request.user)
    logout(request)
    print(request.user)
    return JsonResponse({"result": {"status": "ok"}})


def userView(request: HttpRequest):
    print(request.user)
    user = authenticate(request)
    return JsonResponse({"result": {"status": "ok"}})
