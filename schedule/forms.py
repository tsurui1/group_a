from django import forms
from .models import Schedule


class ScheduleForm(forms.ModelForm):
    datetime = forms.SplitDateTimeField(
        label='日時',
        required=False,
        widget=forms.SplitDateTimeWidget(date_attrs={'type': 'date'}, time_attrs={'type': 'time'})
    )

    class Meta:
        model = Schedule
        # fields = ('title', 'duration_begin', 'duration_end', 'datetime', 'place', 'memo', 'image', 'budget', )
        fields = '__all__'
        widgets = {
            'duration_begin': forms.NumberInput(attrs={
                "type": "date"
            }),
            'duration_end': forms.NumberInput(attrs={
                "type": "date"
            })
        }
