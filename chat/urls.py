from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'chat'
urlpatterns = [
    path('<int:pk>/', login_required(views.ChatView.as_view()), name='chat_top'),
]
