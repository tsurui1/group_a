from django.shortcuts import redirect, render
from django.views import generic
from django.urls import reverse_lazy
from .models import Schedule
from .forms import ScheduleForm


class ScheduleListView(generic.ListView):
    model = Schedule
    template_name = 'schedule/schedule_list.html'


class ScheduleCreateView(generic.CreateView):
    model = Schedule
    form_class = ScheduleForm
    template_name = 'schedule/schedule_create.html'
    success_url = reverse_lazy('schedule:schedule_create')
