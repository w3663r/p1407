from .models import (Person, Connection, Homework, Meeting) 
from rest_framework import serializers,viewsets,status, generics

class PersonSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Person
        fields = '__all__'

class ConnectionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Connection
        fields = '__all__'

class HomeworkSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Homework
        fields = '__all__'

class MeetingSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Meeting
        fields = '__all__'




