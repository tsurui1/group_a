from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *

app_name = 'article'

urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    path('create/', ArticleCreateView.as_view(), name='article_create'),
    path('detail/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('update/<int:pk>/', ArticleUpdateView.as_view(), name='article_update'),
    path('delete/<int:pk>/', ArticleDeleteView.as_view(), name='article_delete'),
]