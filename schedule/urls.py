from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'schedule'
urlpatterns = [
    path('', login_required(views.ScheduleListView.as_view()), name='schedule_list'),
    path('schedule_create/', login_required(views.ScheduleCreateView.as_view()), name='schedule_create'),
    path('schedule_update/<int:pk>/', login_required(views.ScheduleUpdateView.as_view()), name='schedule_update'),
    path('schedule_delete/<int:pk>/', login_required(views.ScheduleDeleteView.as_view()), name='schedule_delete'),
    path('schedule_detail/<int:pk>/', login_required(views.ScheduleDetailView.as_view()), name='schedule_detail'),
    path('plan_create/<int:pk>/', login_required(views.PlanCreateView.as_view()), name='plan_create'),
    path('plan_update/<int:pk>/', login_required(views.PlanUpdateView.as_view()), name='plan_update'),
    path('plan_delete/<int:pk>/', login_required(views.PlanDeleteView.as_view()), name='plan_delete'),
]
