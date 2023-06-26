from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    categories = forms.CharField(label='カテゴリ', required=False)
    class Meta:
        model = Article
        fields = ('title', 'image', 'text', 'date_begin', 'date_end',
                  'state_flag', 'categories')

        widgets = {
            'date_begin': forms.NumberInput(attrs={
                "type": "date"
            }),
            'date_end': forms.NumberInput(attrs={
                "type": "date"
            }),
        }



class SearchForm(forms.Form):
    keyword = forms.CharField(label='キーワードで検索', required=False)