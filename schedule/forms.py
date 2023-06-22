from django import forms
from .models import Schedule


class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ('date', 'time', 'place', 'memo', 'image', 'budget', )
