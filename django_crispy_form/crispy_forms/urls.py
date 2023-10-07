from .views import todo_view
from django.urls import path

urlpatterns = [
    path('todo',todo_view, name="todo"),
]