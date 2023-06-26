from django import forms
from .models import Schedule, Plan


class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ('title', 'duration_begin', 'duration_end', 'total_budget',)
        widgets = {
            'duration_begin': forms.NumberInput(attrs={
                "type": "date"
            }),
            'duration_end': forms.NumberInput(attrs={
                "type": "date"
            })
        }


class PlanForm(forms.ModelForm):
    datetime = forms.SplitDateTimeField(
        label='日時',
        required=False,
        widget=forms.SplitDateTimeWidget(date_attrs={'type': 'date'}, time_attrs={'type': 'time'})
    )

    class Meta:
        model = Plan
        fields = ('datetime', 'image', 'place', 'budget', 'memo')


