from django.urls import path

from .views import login_view, MemoriesView

urlpatterns = [
    path('memories/', MemoriesView.as_view(), name='memories'),
    path('memories/log', login_view, name='log'),
]
