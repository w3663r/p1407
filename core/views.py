from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import PersonSerializer, ConnectionSerializer, HomeworkSerializer, MeetingSerializer
from .models import Person, Connection, Homework, Meeting

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class ConnectionViewSet(viewsets.ModelViewSet):
    queryset = Connection.objects.all()
    serializer_class = ConnectionSerializer

class HomeworkViewSet(viewsets.ModelViewSet):
    queryset = Homework.objects.all()
    serializer_class = HomeworkSerializer

class MeetingViewSet(viewsets.ModelViewSet):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer

from functools import wraps

from rest_framework.decorators import api_view
from django.http import JsonResponse

def public(request):
    return JsonResponse({'message': 'Hello from a public endpoint! You don\'t need to be authenticated to see this.'})


@api_view(['GET'])
def private(request):
    return JsonResponse({'message': 'Hello from a private endpoint! You need to be authenticated to see this.'})

def index(request):
	context={'info':'some info'}
	return render(request,'core/index.html',context)


