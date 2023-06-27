from django.shortcuts import redirect, render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from .models import CustomUser
from .forms import CustomUserForm, UpdateForm, ManagementUserForm
from schedule.models import Schedule


class AccountCreateView(generic.CreateView):
    model = CustomUser
    form_class = CustomUserForm
    template_name = 'accounts/accounts_create.html'
    success_url = reverse_lazy('article:article_list')

class Login(LoginView):
    template_name = 'accounts/login.html'

class Logout(LogoutView):
    next_page = reverse_lazy('article:article_list')

class MyPageView(generic.ListView):
    model = CustomUser
    template_name = 'accounts/my_page.html'

    def get_queryset(self):
        queryset = Schedule.objects.order_by('duration_begin')
        queryset = queryset.filter(users=self.request.user)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['schedule_list'] = Schedule.objects.all()

        return context

class MyPageUpdateView(generic.UpdateView):
    model = CustomUser
    form_class = UpdateForm
    template_name = 'accounts/update.html'
    success_url = reverse_lazy('accounts:my_page')

    def get_object(self):
        return self.request.user

class ManagementUserCreateView(generic.CreateView):
    model = CustomUser
    form_class = ManagementUserForm
    template_name = 'accounts/management_create.html'
    success_url = reverse_lazy('article:article_list')

class ManagementUserLoginView(LoginView):
    template_name = 'accounts/management_login.html'
    next_page = reverse_lazy('article:management_list')