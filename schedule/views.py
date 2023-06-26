from django.shortcuts import redirect, render
from django.views import generic
from django.urls import reverse_lazy
from .models import Schedule, Plan
from .forms import ScheduleForm, PlanForm
from django.db.models import Sum


class ScheduleListView(generic.ListView):
    model = Schedule
    template_name = 'schedule/schedule_list.html'


class ScheduleCreateView(generic.CreateView):
    model = Schedule
    form_class = ScheduleForm
    template_name = 'schedule/schedule_create.html'
    success_url = reverse_lazy('schedule:schedule_list')


class ScheduleUpdateView(generic.UpdateView):
    model = Schedule
    form_class = ScheduleForm
    template_name = 'schedule/schedule_update.html'
    success_url = reverse_lazy('schedule:schedule_list')


class ScheduleDeleteView(generic.DeleteView):
    model = Schedule
    template_name = 'schedule/schedule_delete.html'
    success_url = reverse_lazy('schedule:schedule_list')


class ScheduleDetailView(generic.DetailView):
    model = Schedule
    template_name = 'schedule/schedule_detail.html'


    # a=Plan.objects.aggregate(Sum('budget'))
    # print(a)


class PlanCreateView(generic.CreateView):
    model = Plan
    form_class = PlanForm
    template_name = 'schedule/plan_create.html'
    success_url = reverse_lazy('schedule:schedule_list')

    def form_valid(self, form):
        plan = form.save(commit=False)
        plan.schedule = Schedule.objects.get(pk=self.kwargs['pk'])
        plan.save()
        return redirect('schedule:schedule_detail', pk=plan.schedule.pk)


class PlanUpdateView(generic.UpdateView):
    model = Plan
    form_class = PlanForm
    template_name = 'schedule/plan_update.html'
    success_url = reverse_lazy('schedule:schedule_list')

    def get_success_url(self):
        plan = self.get_object()
        return reverse_lazy('schedule:schedule_detail', kwargs={'pk': plan.schedule.pk})


class PlanDeleteView(generic.DeleteView):
    model = Plan
    template_name = 'schedule/plan_delete.html'
    success_url = reverse_lazy('schedule:schedule_list')

    def get_success_url(self):
        plan = self.get_object()
        return reverse_lazy('schedule:schedule_detail', kwargs={'pk': plan.schedule.pk})

