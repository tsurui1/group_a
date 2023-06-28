from django import forms
from .models import Chat


class ChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ('comment', 'image')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['comment'].widget.attrs = {'placeholder': 'コメント', 'class': 'input-field'}
