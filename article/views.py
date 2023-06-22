from django.shortcuts import resolve_url, render
from django.views import generic
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Article
from .forms import ArticleForm, SearchForm


class ArticleListView(generic.ListView):
    model = Article
    template_name = 'article/article_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SearchForm
        return context

    def get_queryset(self):
        queryset = Article.objects.all()

        keyword = self.request.GET.get('keyword')
        if keyword:
            queryset = queryset.filter(
                Q(title__icontains=keyword) | Q(text__icontains=keyword) | Q(categories__name__icontains=keyword)
            )
        return queryset

class ArticleCreateView(generic.CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'article/article_create.html'
    success_url = reverse_lazy('article:article_list')

class ArticleDetailView(generic.DetailView):
    model = Article
    template_name = 'article/article_detail.html'

class ArticleUpdateView(generic.UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'article/article_update.html'

    def get_success_url(self):
        return resolve_url('article:article_detail', pk=self.kwargs['pk'])

class ArticleDeleteView(generic.DeleteView):
    model = Article
    template_name = 'article/article_delete.html'
    success_url = reverse_lazy('article:article_list')