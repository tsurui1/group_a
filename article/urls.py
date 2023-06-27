from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *

app_name = 'article'

urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    path('detail/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('create/', login_required(ArticleCreateView.as_view()), name='article_create'),
    path('update/<int:pk>/', login_required(ArticleUpdateView.as_view()), name='article_update'),
    path('delete/<int:pk>/', login_required(ArticleDeleteView.as_view()), name='article_delete'),

    path('management/list/', login_required(ManagementListView.as_view()), name='management_list'),
]