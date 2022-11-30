from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.urls import reverse
from django.views.generic import ListView, CreateView

from main_app.models import Memory


class MemoriesView(ListView):
    model = Memory
    template_name = 'main.html'
    context_object_name = 'memory'

    def get_queryset(self):
        return get_list_or_404(Memory, author__id=self.request.user.id)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()

        current_user = get_object_or_404(User, id=self.request.user.id)
        context['first_name'] = current_user.first_name
        context['last_name'] = current_user.last_name

        memories = Memory.objects.filter(author__id=current_user.id)
        coordinates = [[memory.location.x, memory.location.y] for memory in memories]
        context["coordinates"] = coordinates
        return context


class MemoryCreateView(CreateView):
    model = Memory
    template_name = 'addmemory.html'
    fields = ['title', 'description', 'location']

    def get_success_url(self):
        return reverse('memories')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def login_view(request):
    return render(request, 'login.html')