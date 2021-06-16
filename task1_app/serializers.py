from django.db.models import fields
from rest_framework import serializers


from .models import task1,task2

from .models import task1,yes_complaines_login



class get_db(serializers.ModelSerializer):
    class Meta:
        model=task1
        fields='__all__'
