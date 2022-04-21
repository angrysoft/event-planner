from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path("login", csrf_exempt(views.LoginView.as_view()), name="login"),
    path("logout", csrf_exempt(views.logoutView), name="login"),
    path("user", views.userView, name="user"),
]
