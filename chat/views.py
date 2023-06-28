from django.shortcuts import redirect
from django.views import generic
from .models import Chat
from schedule.models import Schedule
from .forms import ChatForm


class ChatView(generic.CreateView):
    model = Chat
    form_class = ChatForm
    template_name = 'chat/chat_top.html'

    def dispatch(self, request, *args, **kwargs):
        """スケジュールメンバーだけが参加できる、メンバー以外はリダイレクト先へ"""
        schedule = Schedule.objects.get(pk=self.kwargs['pk'])
        if self.request.user in schedule.users.all():
            return super().dispatch(request, *args, **kwargs)
        return redirect('schedule:schedule_list')

    def get_context_data(self, **kwargs):
        """テンプレートファイルに渡す + フィルターで絞り込み（スケジュール:detail/pk）"""
        context = super().get_context_data(**kwargs)
        context['schedule'] = Schedule.objects.get(pk=self.kwargs['pk'])
        context['chat_list'] = Chat.objects.filter(groups=Schedule.objects.get(pk=self.kwargs['pk'])).order_by('-created_at')
        return context

    def form_valid(self, form):
        """データの送信"""
        schedule = Schedule.objects.get(pk=self.kwargs['pk'])
        chat = form.save(commit=False)
        chat.user = self.request.user
        chat.groups = schedule
        chat.save()
        return redirect('chat:chat_top', pk=schedule.pk)
