from django.shortcuts import redirect, render
from django.views import generic
from django.urls import reverse_lazy
from .models import Schedule
from .forms import ScheduleForm


class ScheduleListView(generic.ListView):
    model = Schedule
    template_name = 'schedule_list.html'
