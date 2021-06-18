from .models import Airplanes, AirplaneStatus
from rest_framework import serializers


class AirplaneSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="airplanes-detail")
    status = serializers.HyperlinkedRelatedField(view_name="statuses-detail", queryset=AirplaneStatus.objects.all())
    status_name = serializers.ReadOnlyField(source="status.status")

    class Meta:
        model = Airplanes
        fields = ['url', 'id', 'model', 'range', 'engines', 'capacity', 'status', 'status_name']


class StatusSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="statuses-detail")

    class Meta:
        model = AirplaneStatus
        fields = ['url', 'id', 'status']