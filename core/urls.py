from django.contrib import admin
from django.urls import path, include
from .views import index
from rest_framework.routers import DefaultRouter 
from .views import PersonViewSet, ConnectionViewSet, HomeworkViewSet, MeetingViewSet, public, private

router = DefaultRouter()
router.register('person', PersonViewSet, base_name='person') 
router.register('connection', ConnectionViewSet, base_name='connection') 
router.register('homework', HomeworkViewSet, base_name='homework') 
router.register('meeting', MeetingViewSet, base_name='meeting') 

urlpatterns = [
	path('', index),
    path('api/public', public),
    path('api/private', private),
]

urlpatterns += router.urls

