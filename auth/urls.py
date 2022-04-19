from django.urls import path
import views

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.logout, name="login"),
]
