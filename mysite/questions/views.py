# todos/views.py
from rest_framework import generics

from . import models
from . import serializers


class ListTodo(generics.ListCreateAPIView):
    queryset = models.Question.objects.all()
    serializer_class = serializers.TodoSerializer


class ListTodo2(generics.ListCreateAPIView):
    queryset = models.Choice.objects.all()
    serializer_class = serializers.TodoSerializer2


class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Question.objects.all()
    serializer_class = serializers.TodoSerializer
