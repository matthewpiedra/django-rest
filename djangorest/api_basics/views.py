from typing import final
from django.shortcuts import render
from rest_framework.serializers import Serializer
from .serializers import AirplaneSerializer, StatusSerializer
from .models import Airplane, Status
from rest_framework import views, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

# Create your views here.


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'airplanes': reverse('airplanes-list', request=request, format=format),
        'statuses': reverse('statuses-list', request=request, format=format)
    })


class AirplaneViewSet(viewsets.ModelViewSet):
    serializer_class = AirplaneSerializer

    def get_queryset(self):
        req = self.request
        s = req.query_params.get('status')

        airplanes = Airplane.objects.all()
        
        if s:
            airplanes = Airplane.objects.filter(status__status=s)
            return airplanes
     
        return airplanes

    def create(self, request, *args, **kargs):
        a_data = request.data  

        new_airplane = Airplane.objects.create(
            model=a_data['model'],
            range=a_data['range'],
            engines=a_data['engines'],
            capacity=a_data['capacity'],
            status=Status.objects.get(status=a_data['status'])
        )

        serializer = AirplaneSerializer(new_airplane, context={'request': request})
        
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        airplane_object = self.get_object() # previous object data

        changed_data = request.data
        
        if 'status' not in changed_data or changed_data['status'] == '':
            status = airplane_object.status
        elif changed_data['status'] != 'ACTIVE' and changed_data['status'] != 'RETIRED' and changed_data['status'] != 'BROKEN' and changed_data['status'] != 'NEW':
            pk = int(changed_data['status'].split('/')[-2]) # get id from end of hyperlink url
            
            status = Status.objects.get(pk=pk)
        else:
            status = Status.objects.get(status=changed_data['status'])
        
        airplane_object.status = status
        airplane_object.model = changed_data['model'] if 'model' in changed_data and changed_data['model'] != '' else airplane_object.model
        airplane_object.range = changed_data['range'] if 'range' in changed_data and changed_data['range'] != '' else airplane_object.range
        airplane_object.engines = changed_data['engines'] if 'engines' in changed_data and changed_data['engines'] != '' else airplane_object.engines
        airplane_object.capacity = changed_data['capacity'] if 'capacity' in changed_data and changed_data['capacity'] != '' else airplane_object.capacity

        serializer = AirplaneSerializer(airplane_object, context={'request': request})

        return Response(serializer.data)

        

class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
