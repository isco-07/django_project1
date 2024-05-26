from django.contrib.auth.views import LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import (
    RegisterView,
    LoginUser,
    email_verification,
    password_reset_request,
    password_reset_done,
)

app_name = UsersConfig.name
urlpatterns = [
    path("login/", LoginUser.as_view(template_name="users/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
    path("email-confirm/<str:token>/", email_verification, name="email-confirm"),
    path("password_reset/", password_reset_request, name="password_reset"),
    path("password_reset_done/", password_reset_done, name="password_reset_done"),
]
