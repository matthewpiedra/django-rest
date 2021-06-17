from .models import Airplane, Status
from rest_framework import serializers


class AirplaneSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="airplanes-detail")
    status = serializers.HyperlinkedRelatedField(view_name="statuses-detail", queryset=Status.objects.all())
    status_name = serializers.ReadOnlyField(source="status.status")

    class Meta:
        model = Airplane
        fields = ['url', 'airplane_id', 'model', 'range', 'engines', 'capacity', 'status', 'status_name', 'last_updated']


class StatusSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="statuses-detail")

    class Meta:
        model = Status
        fields = ['url', 'status_id', 'status']