from django.urls import path

from .views import TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path('', TaskListView.as_view(), name='index'),
    path('add_tasks/', TaskCreateView.as_view(), name='add_tasks'),
    path('task/<int:pk>/', TaskUpdateView.as_view(), name='tasks_update'),
    path('delete/<int:pk>/',TaskDeleteView.as_view(), name='tasks_delete'),
]