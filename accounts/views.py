from django.shortcuts import redirect, render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from .models import CustomUser
from .forms import CustomUserForm, UpdateForm


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

class MyPageUpdateView(generic.UpdateView):
    model = CustomUser
    form_class = UpdateForm
    template_name = 'accounts/update.html'
    success_url = reverse_lazy('accounts:my_page')

    def get_object(self):
        return self.request.user