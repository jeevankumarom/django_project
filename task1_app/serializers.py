from django.db.models import fields
from rest_framework import serializers

from .models import task1,task2


class get_db(serializers.ModelSerializer):
    class Meta:
        model=task1
        fields='__all__'

class get(serializers.ModelSerializer):
    class Meta:
        model=task2
        fields='__all__'