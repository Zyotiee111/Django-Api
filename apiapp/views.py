from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TestSerializer
from .models import Test

# Create your views here.
@api_view(['GET'])
def apioverview(request):
    api_urls = {
        'List': '/tasklist/',
        'Detail View': '/taskdetail/<str:pk>/',
        'Create':'/taskcreate',
        'Update': '/taskupdate/<str:pk>',
        'Delete': '/taskdelete/<str:pk>',
    }
    return Response(api_urls)

@api_view(['GET'])
def TaskList(request):
    tasks = Test.objects.all()
    serializer = TestSerializer(tasks, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def TaskDetail(request,pk):
    tasks = Test.objects.get(id = pk)
    serializer = TestSerializer(tasks, many = False)
    return Response(serializer.data)

@api_view(['POST'])
def TaskCreate(request):
    serializer = TestSerializer(data= request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def TaskUpdate(request,pk):
    tasks = Test.objects.get(id = pk)
    serializer = TestSerializer(instance = tasks,data= request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def TaskDelete(request,pk):
    task = Test.objects.get(id =pk)
    task.delete()
    return Response("Successfully deleted!")



