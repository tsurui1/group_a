from django.shortcuts import resolve_url, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Article, Category
from .forms import ArticleForm, SearchForm
import datetime


class ArticleListView(generic.ListView):
    model = Article
    template_name = 'article/article_list.html'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SearchForm
        return context

    def get_queryset(self):
        queryset = Article.objects.all()

        dt_now = datetime.datetime.now()
        queryset = queryset.filter(date_end__gte=dt_now, date_begin__lte=dt_now)
        #  Scheduleで保存したカテゴリーを呼び出す

        keyword = self.request.GET.get('keyword')
        if keyword:
            queryset = queryset.filter(
                Q(title__icontains=keyword) | Q(text__icontains=keyword) |
                Q(categories__name__icontains=keyword)
            )
        return queryset

class ArticleCreateView(generic.CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'article/article_create.html'
    success_url = reverse_lazy('article:article_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        return context

    def form_valid(self, form):
        article = form.save(commit=False)

        article.user = self.request.user

        text = self.request.POST['categories']
        # text = article.categories
        text_list = text.split(',')

        article.save()

        for category in text_list:
            print(category)
            if category.startswith(','):
                if Category.objects.filter(name=category).exists():
                    add_category = Category.objects.filter(name=category).first()
                    article.categories.add(add_category)

                else:
                    add_category = Category.objects.create(name=category)
                    article.categories.add(add_category)

        return redirect('article:article_list')



class ArticleDetailView(generic.DetailView):
    model = Article
    template_name = 'article/article_detail.html'

class ArticleUpdateView(generic.UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'article/article_update.html'

    def get_success_url(self):
        return resolve_url('article:article_detail', pk=self.kwargs['pk'])

    def form_valid(self, form):
        article = form.save(commit=False)

        article.user = self.request.user

        text = self.request.POST['categories']
        # text = article.categories
        text_list = text.split(',')

        article.save()

        for category in text_list:
            print(category)
            if category.startswith(','):
                if Category.objects.filter(name=category).exists():
                    add_category = Category.objects.filter(name=category).first()
                    article.categories.add(add_category)

                else:
                    add_category = Category.objects.create(name=category)
                    article.categories.add(add_category)

        return redirect('article:article_list')

    def get_initial(self):
        categories = ''
        for category in self.object.categories.all():
            categories += f',{category.name}'
        initial_dict = {'categories': categories}
        return initial_dict

class ArticleDeleteView(generic.DeleteView):
    model = Article
    template_name = 'article/article_delete.html'
    success_url = reverse_lazy('article:article_list')