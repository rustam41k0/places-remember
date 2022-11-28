from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView
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

        memories = Memory.objects.all()
        coords = [[memory.location.x, memory.location.y] for memory in memories]
        context["coordinates"] = coords
        return context


class MemoryCreateView(CreateView):
    model = Memory
    template_name = 'addmemory.html'
    fields = ['title', 'description', 'location']


def login_view(request):
    return render(request, 'login.html')
