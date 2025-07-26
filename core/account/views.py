from .forms import AuthenticationForm
from django.shortcuts import render
from django.contrib.auth import views as auth_views


# Create your views here.

class LoginView(auth_views.LoginView):
    redirect_authenticated_user = True


class LogoutView(auth_views.LogoutView):
    pass
