from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser

class CustomUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'birthday', 'username')

        widgets = {
            'birthday': forms.NumberInput(attrs={"type": "date"}),
        }

class UpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('bio', 'username')

class ManagementUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'is_staff')