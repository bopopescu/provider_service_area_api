from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from service_area.models import ServiceArea
from provider.serializer import ProviderSerializer
from provider.models import Provider


class ServiceAreaSerializer(GeoFeatureModelSerializer):

    class Meta:
        model = ServiceArea
        fields = ('id', 'provider_name', 'name', 'price', 'provider')
        geo_field = 'polygons'


class PointSerializer(serializers.Serializer):

    lat = serializers.FloatField()
    long = serializers.FloatField()
