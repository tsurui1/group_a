from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'schedule'
urlpatterns = [
    path('', views.ScheduleListView.as_view(), name='schedule_list'),
    path('schedule_create/', views.ScheduleCreateView.as_view(), name='schedule_create'),
    path('schedule_detail/<int:pk>/', views.ScheduleDetailView.as_view(), name='schedule_detail'),
    path('plan_create/', views.PlanCreateView.as_view(), name='plan_create'),
    # path('plan_update/<int:pk>/', views.PlanUpdateView.as_view(), name='plan_update'),
]
