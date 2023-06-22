from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'image', 'text', 'date_begin', 'date_end',
                  'state_flag', 'categories')

class SearchForm(forms.Form):
    keyword = forms.CharField(label='キーワードで検索', required=False)