from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import task1, task2
from django.http import JsonResponse
from .serializers import get_db,get
from rest_framework import viewsets

from task1_app import serializers

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



class taskViewset(viewsets.ModelViewSet):
    queryset = task1.objects.all()
    serializer_class = get_db

    def list(self,request):
        name=request.GET['name']
        queryset=task1.objects.filter(name=name)
        serializer_class = get_db(queryset,many=True)
        print(serializer_class.data)
        return Response(serializer_class.data)
    


@api_view(['POST'])
def goto(request):
    query=task2.objects.all()
    print(query)
    serializer_class=get(data=request.data)
    
    if serializer_class.is_valid():
        serializer_class.save()
    return Response(serializer_class.data)

@api_view(['post'])
def file_upload(request):
    if request.method == 'POST':
        
        forr=request.POST['forr']
        
        file=request.FILES['file']
        
        print(file,forr)

    return Response("file uploaded")



