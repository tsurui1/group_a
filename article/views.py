from django.shortcuts import render
from django.views import generic
from .models import Article

class ArticleListView(generic.ListView):
    model = Article
    template_name = 'article/article_list.html'