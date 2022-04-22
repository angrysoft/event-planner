from functools import wraps
from django.contrib.auth import authenticate
from django.http import HttpRequest, JsonResponse


def auth_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request: HttpRequest, *args, **kwargs):
        user = authenticate(request)
        if user:
            request.user = user
            return view_func(request, *args, **kwargs)
        else:
            return JsonResponse({"results": {}, "errors": "Authenications faild"}, status=400)

    return _wrapped_view
