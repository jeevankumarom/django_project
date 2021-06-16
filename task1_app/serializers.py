from rest_framework import serializers

from .models import task1,yes_complaines_login


class get_db(serializers.ModelSerializer):
    class Meta:
        model=task1
        fields='__all__'


class login_serializers(serializers.ModelSerializer):
    class Meta:
        model=yes_complaines_login
        fields='__all__'