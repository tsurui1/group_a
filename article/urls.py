from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *

app_name = 'article'

urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
]