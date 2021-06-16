from django.db import models

class task1(models.Model):
    name=models.CharField(max_length=100)
    password=models.CharField(max_length=100)


class yes_complaines_login(models.Model):
    user_name=models.CharField(max_length=100)
    password=models.CharField(max_length=100)