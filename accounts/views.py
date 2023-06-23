from django.shortcuts import redirect, render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from .models import CustomUser
from .forms import CustomUserForm


class AccountCreateView(generic.CreateView):
    model = CustomUser
    form_class = CustomUserForm
    template_name = 'accounts/accounts_create.html'
    success_url = reverse_lazy('article:article_list')

class Login(LoginView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('article:article_list')

class Logout(LogoutView):
    next_page = reverse_lazy('article:article_list')

class MyPageView(generic.ListView):
    model = CustomUser
    template_name = 'accounts/my_page.html'