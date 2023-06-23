from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'schedule'
urlpatterns = [
    path('<int:pk>', views.ScheduleListView.as_view(), name='schedule_list'),
    path('schedule_create/', views.ScheduleCreateView.as_view(), name='schedule_create'),
    path('plan_create/', views.PlanCreateView.as_view(), name='plan_create'),

]
