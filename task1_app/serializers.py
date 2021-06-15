from rest_framework import serializers

from .models import task1


class get_db(serializers.ModelSerializer):
    class Meta:
        model=task1
        fields='__all__'