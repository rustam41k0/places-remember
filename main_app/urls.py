from django.urls import path

from .views import login_view, logout_user, MemoriesView

urlpatterns = [
    path('memories/', MemoriesView.as_view(), name='memories'),
    path('memories/log', login_view, name='log'),
    path('logout/', logout_user, name='logout'),
]
