from rest_framework import viewsets
from rest_framework.decorators import action

from tasks.models import Task
from tasks.serializers import (TaskSerializer)

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = []
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['title', 'description']
    filterset_fields = ['completed']