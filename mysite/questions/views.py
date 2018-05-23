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


from drf_multiple_model.views import ObjectMultipleModelAPIView
from drf_multiple_model.views import FlatMultipleModelAPIView


class TextAPIView(ObjectMultipleModelAPIView):
    querylist = [
        {'queryset': models.Question.objects.filter(), 'serializer_class': serializers.TodoSerializer},
        {'queryset': models.Choice.objects.filter(), 'serializer_class': serializers.TodoSerializer2}
    ]

