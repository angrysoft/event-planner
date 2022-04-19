import imp
from typing import Any, Dict
from django.http import HttpRequest, JsonResponse
from django.views import View
from auth.models import User
from .forms import LoginForm
from django.contrib.auth import authenticate
import jwt
import uuid
from django.conf import settings


class LoginView(View):
    def post(self, request: HttpRequest):
        login_form = LoginForm(request.POST)
        results: Dict[str, Any] = {"result": {}}
        if login_form.is_valid():
            user = authenticate(
                username=login_form.cleaned_data("login"),
                password=login_form.cleaned_data("password"),
            )
            if user is not None:
                results["result"] = self.generate_auth_tokens(user)
        else:
            results["erros" : login_form.errors.as_json()]

        return JsonResponse(results)

    def generate_auth_token(self, user: User) -> str:
        token: str = jwt.encode(
            {"user": user.username, "token": uuid.uuid4()},
            settings.JWTKEY,
            algorithm="HS256",
        )
        return token


def logout(request: HttpRequest):
    return JsonResponse({"result": {"status": "ok"}})
