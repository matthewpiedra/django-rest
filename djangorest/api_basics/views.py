from django.shortcuts import render
from rest_framework.serializers import Serializer
from .serializers import AirplaneSerializer, StatusSerializer
from .models import Airplanes, AirplaneStatus
from rest_framework import views, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.exceptions import NotFound, ParseError
from urllib.parse import urlparse, parse_qs

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

        raw_parameters = urlparse(req.get_full_path())
        parameters = parse_qs(raw_parameters.query)

        airplanes = Airplanes.objects.all()
        
        if len(parameters.items()) == 1: # only expecting one parameter
            if 'status' not in parameters: # only expecting the status parameter
                raise NotFound("Invalid Parameter")
            elif s != 'ACTIVE' and s != 'RETIRED' and s != 'BROKEN' and s != 'NEW':
                raise NotFound('Invalid value for status. Try again with either ACTIVE, RETIRED, NEW, or BROKEN')

            airplanes = Airplanes.objects.filter(status__status=s)

            return airplanes
        elif len(parameters.items()) > 1: # if there's more than one param, then it's automaticaly invalid
            raise NotFound('Only expecting one paramater: status')
     
        return airplanes

    def create(self, request, *args, **kargs):
        a_data = request.data

        status = a_data['status']

        if not isinstance(status, str):
            raise ParseError("Invalid field type for status")
        elif not AirplaneStatus.objects.filter(status=status).exists():
            raise ParseError("Invalid field value for status")

        new_airplane = Airplanes.objects.create(
            model=a_data['model'],
            range=a_data['range'],
            engines=a_data['engines'],
            capacity=a_data['capacity'],
            status=AirplaneStatus.objects.get(status=status)
        )

        serializer = AirplaneSerializer(new_airplane, context={'request': request})
        
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        airplane_object = self.get_object() # previous object data

        changed_data = request.data

        if 'status' not in changed_data or changed_data['status'] == '':
            status = airplane_object.status
        elif changed_data['status'] != 'ACTIVE' and changed_data['status'] != 'RETIRED' and changed_data['status'] != 'BROKEN' and changed_data['status'] != 'NEW':
            raise ParseError("Invalid value for status")
        else:
            status = AirplaneStatus.objects.get(status=changed_data['status'])
        
        airplane_object.status = status
        airplane_object.model = changed_data['model'] if 'model' in changed_data and changed_data['model'] != '' else airplane_object.model
        airplane_object.range = changed_data['range'] if 'range' in changed_data and changed_data['range'] != '' else airplane_object.range
        airplane_object.engines = changed_data['engines'] if 'engines' in changed_data and changed_data['engines'] != '' else airplane_object.engines
        airplane_object.capacity = changed_data['capacity'] if 'capacity' in changed_data and changed_data['capacity'] != '' else airplane_object.capacity

        serializer = AirplaneSerializer(airplane_object, context={'request': request})

        return Response(serializer.data)

        

class StatusViewSet(viewsets.ModelViewSet):
    queryset = AirplaneStatus.objects.all()
    serializer_class = StatusSerializer
