from django.shortcuts import resolve_url, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Article, Category
from .forms import ArticleForm, SearchForm
from schedule.models import Schedule
import datetime


class ArticleListView(generic.ListView):
    model = Article
    template_name = 'article/article_list.html'
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SearchForm(self.request.GET)
        if self.request.user.is_authenticated:
            schedule_list = Schedule.objects.filter(users=self.request.user).values_list('id', flat=True)
            category_list = Schedule.categories.through.objects.filter(schedule_id__in=schedule_list).values_list('category_id', flat=True)
            category_list = Category.objects.filter(id__in=category_list)
            context['category_list'] = category_list

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
            ).distinct()
        return queryset


class ArticleCreateView(generic.CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'article/article_create.html'
    success_url = reverse_lazy('article:management_list')

    def get(self, request):
        if not request.user.is_staff:
            return redirect("accounts:login")
        return super().get(request)

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

        return redirect('article:management_list')


class ArticleDetailView(generic.DetailView):
    model = Article
    template_name = 'article/article_detail.html'


class ArticleUpdateView(generic.UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'article/article_update.html'
    success_url = reverse_lazy('article:management_list')

    def get(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect("accounts:login")
        return super().get(request, *args, **kwargs)

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

        return redirect('article:management_list')

    def get_initial(self):
        categories = ''
        for category in self.object.categories.all():
            categories += f',{category.name}'
        initial_dict = {'categories': categories}
        return initial_dict


class ArticleDeleteView(generic.DeleteView):
    model = Article
    template_name = 'article/article_delete.html'
    success_url = reverse_lazy('article:management_list')

    def get(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect("accounts:login")
        return super().get(request, *args, **kwargs)


class ManagementListView(generic.ListView):
    model = Article
    template_name = 'article/management_list.html'
    paginate_by = 4

    def get(self, request):
        if not request.user.is_staff:
            return redirect("accounts:login")
        return super().get(request)

    def get_queryset(self):
        queryset = Article.objects.order_by('-created_at')
        queryset = queryset.filter(user=self.request.user)

        return queryset
