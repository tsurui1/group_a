from django import forms
from .models import Chat, Schedule


class ChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ('comment',)
