from django.shortcuts import render, redirect
from django.views.generic import ListView
from main_app.models import Memory


class MemoriesView(ListView):
    model = Memory
    template_name = 'main.html'
    context_object_name = 'memory'

    def get_queryset(self):
        return Memory.objects.filter(author__id=self.request.user.id)


def login_view(request):
    return render(request, 'login.html')


def logout_user(request):
    return redirect('log')
