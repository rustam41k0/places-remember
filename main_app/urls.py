from django.urls import path

from .views import login_view, MemoriesView, MemoryCreateView

urlpatterns = [
    path('memories/', MemoriesView.as_view(), name='memories'),
    path('sign-in/', login_view, name='sign_in'),
    path('add-memory/', MemoryCreateView.as_view(), name='memory_create'),
]
