# questions/serializers.py
from rest_framework import serializers
from . import models


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('__all__')
        model = models.Question


class TodoSerializer2(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'question',
            'choice_text',
            'compliance_status',
        )
        model = models.Choice


