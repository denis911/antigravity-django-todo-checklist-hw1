from django.urls import path
from . import views

urlpatterns = [
    path('', views.TodoListView.as_view(), name='todo-list'),
    path('add/', views.TodoCreateView.as_view(), name='todo-add'),
    path('<int:pk>/edit/', views.TodoUpdateView.as_view(), name='todo-edit'),
    path('<int:pk>/delete/', views.TodoDeleteView.as_view(), name='todo-delete'),
    path('<int:pk>/resolve/', views.toggle_resolved, name='todo-toggle-resolved'),
]
