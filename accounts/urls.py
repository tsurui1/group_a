from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

app_name = 'accounts'

urlpatterns = [
    path('create/', AccountCreateView.as_view(), name='accounts_create'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),

    path('page/', MyPageView.as_view(), name='my_page'),
    path('update/', MyPageUpdateView.as_view(), name='my_page_update'),

    # path('management/', ManagementCreateView.as_view(), name='')
]