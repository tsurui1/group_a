from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

app_name = 'accounts'

urlpatterns = [
    path('create/', AccountCreateView.as_view(), name='accounts_create'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),

    # path('page/', login_required(MyPageView.as_view()), name='my_page'),
    path('update/', login_required(MyPageUpdateView.as_view()), name='my_page_update'),

    path('management/create/', ManagementUserCreateView.as_view(), name='management_create'),
    path('management/login/', ManagementUserLoginView.as_view(), name='management_login'),
    # path('management/update/', ManagementUpdateView.as_view(), name='management_update'),
]
