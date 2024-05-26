import random
import secrets
import string

from django.contrib.auth.hashers import make_password
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from users.forms import UserRegisterForm, LoginUserForm, PasswordResetForm
from users.models import User

from config.settings import EMAIL_HOST_USER


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = "users/register.html"
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f"http://{host}/users/email-confirm/{token}/"
        send_mail(
            subject="Подтверждение почты",
            message=f"Перейдите по ссылке для подтверждения почты {url}",
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
        )
        return super().form_valid(form)


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse("users:login"))


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = "users/login.html"


def generate_random_password(length=8):
    characters = string.ascii_letters + string.digits
    return "".join(random.choice(characters) for _ in range(length))


def password_reset_request(request):
    if request.method == "POST":
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            try:
                user = User.objects.get(email=email)
                new_password = generate_random_password()
                user.password = make_password(new_password)
                user.save()

                send_mail(
                    subject="Ваш новый пароль",
                    message=f"Ваш новый пароль: {new_password}",
                    from_email=EMAIL_HOST_USER,
                    recipient_list=[user.email],
                )

                return redirect(reverse("users:password_reset_done"))
            except User.DoesNotExist:
                form.add_error(
                    "email",
                    "Пользователь с этим адресом электронной почты найден не был.",
                )
    else:
        form = PasswordResetForm()

    return render(request, "users/password_reset_form.html", {"form": form})


def password_reset_done(request):
    return render(request, "users/password_reset_done.html")
