from django.db.models import base
from django.urls import path
from .views import AirplaneViewSet, StatusViewSet, api_root

airplanes_list = AirplaneViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

airplanes_detail = AirplaneViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy',
})

statuses_list = StatusViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

statuses_detail = StatusViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy',
})

urlpatterns = [
    path('', api_root),
    path('airplanes/', airplanes_list, name="airplanes-list"),
    path('airplanes/<int:pk>/', airplanes_detail, name="airplanes-detail"),
    path('statuses/', statuses_list, name="statuses-list"),
    path('statuses/<int:pk>/', statuses_detail, name="statuses-detail"),
]