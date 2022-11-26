from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import ListView
from main_app.models import Memory


class MemoriesView(ListView):
    model = Memory
    template_name = 'main.html'
    context_object_name = 'memory'

    def get_queryset(self):
        return Memory.objects.filter(author__id=self.request.user.id)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        current_user = User.objects.get(id=self.request.user.id)
        context['first_name'] = current_user.first_name
        context['last_name'] = current_user.last_name
        return context


def login_view(request):
    return render(request, 'login.html')
