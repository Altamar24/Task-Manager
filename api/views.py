from rest_framework.viewsets import ModelViewSet

from tasks.models import Task
from .serializers import TaskSerializer


class TaskApiViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
