from django.shortcuts import redirect, render
from django.views import generic
from django.urls import reverse_lazy
from .models import Schedule, Plan
from .forms import ScheduleForm, PlanForm
from django.db.models import Sum
from article.models import Category


class ScheduleListView(generic.ListView):
    model = Schedule
    template_name = 'schedule/schedule_list.html'
    queryset = Schedule.objects.all().annotate(sum=Sum('plan__budget'))

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(users=self.request.user)
        return queryset

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_budget'] = Plan.objects.filter(
            schedule=Schedule.objects.get(pk=self.kwargs['pk'])
        ).aggregate(Sum('budget'))['budget__sum']
        return context


class PlanCreateView(generic.CreateView):
    model = Plan
    form_class = PlanForm
    template_name = 'schedule/plan_create.html'
    success_url = reverse_lazy('schedule:schedule_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        return context

    def form_valid(self, form):
        plan = form.save(commit=False)
        plan.schedule = Schedule.objects.get(pk=self.kwargs['pk'])

        plan.user = self.request.user

        category = self.request.POST['categories']
        category_list = category.split(',')

        plan.save()

        for category in category_list:
            print(category)
            if Category.objects.filter(name=category).exists():
                add_category = Category.objects.filter(name=category).first()
                plan.schedule.categories.add(add_category)

            else:
                add_category = Category.objects.create(name=category)
                plan.schedule.categories.add(add_category)

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

