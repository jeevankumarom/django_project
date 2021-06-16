from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import task1,yes_complaines_login
from django.http import JsonResponse
from .serializers import get_db,login_serializers
from rest_framework import viewsets

##vivek
@api_view(['POST'])
def task(request):
    query=task1.objects.all()
    serializers_class=get_db(data=request.data)
    if serializers_class.is_valid():
        serializers_class.save()
    return Response(serializers_class.data)


@api_view(['put'])
def update(request,id):
    query=task1.objects.get(id=id)
    serializers_class=get_db(instance=query,data=request.data,partial=True)
    if serializers_class.is_valid():
        serializers_class.save()
    return Response(serializers_class.data)

##jeeva


class taskViewset(viewsets.ModelViewSet):
    queryset = task1.objects.all()
    serializer_class = get_db

    def list(self,request):
        name=request.GET['name']
        queryset=task1.objects.filter(name=name)
        serializer_class = get_db(queryset,many=True)
        print(serializer_class.data)
        return Response(serializer_class.data)
    

class loginViewset(viewsets.ModelViewSet):
    queryset=yes_complaines_login.objects.all()
    serializer_class=login_serializers

    def list(self,request):
        user_name=request.GET['user_name']
        query=yes_complaines_login.objects.filter(user_name=user_name)
        serializer_class=login_serializers(query,many=True)
        return Response(serializer_class.data)






