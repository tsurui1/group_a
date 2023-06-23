from django.shortcuts import redirect, render
from django.views import generic
from django.urls import reverse_lazy
from .models import Schedule, Plan
from .forms import ScheduleForm, PlanForm


class ScheduleListView(generic.ListView):
    model = Schedule
    template_name = 'schedule/schedule_list.html'


class ScheduleCreateView(generic.CreateView):
    model = Schedule
    form_class = ScheduleForm
    template_name = 'schedule/schedule_create.html'
    success_url = reverse_lazy('schedule:schedule_list')


class ScheduleDetailView(generic.DetailView):
    model = Schedule
    template_name = 'schedule/schedule_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['plan'] = Plan.objects.all().order_by('-datetime')
        return context


class PlanCreateView(generic.CreateView):
    model = Plan
    form_class = PlanForm
    template_name = 'schedule/plan_create.html'
    success_url = reverse_lazy('schedule:schedule_list')
#
#
# class PlanUpdateView(generic.UpdateView):
#     model = Plan
#     form_class = PlanForm
#     template_name = 'schedule/plan_create.html'
#     success_url = reverse_lazy('schedule:schedule_list')
