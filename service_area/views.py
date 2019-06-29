from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response

from django.contrib.gis.geos import Point


from service_area.models import ServiceArea
from service_area.serializer import ServiceAreaSerializer, PointSerializer


class ServiceAreaViewSet(viewsets.ModelViewSet):
    """
    ViewSet for ServiceAreas
    """

    queryset = ServiceArea.objects.order_by('-created')
    serializer_class = ServiceAreaSerializer
    partial = True

    @list_route()
    def find(self, request):
        """
        List of ServiceAreas containing a given Point
        URL params:
            lat: Point latitude
            long: Point longitude
        """
        point = PointSerializer(data=request.GET)
        point.is_valid(raise_exception=True)
        queryset = self.queryset.filter(polygons__intersects=Point(x=point.data['lat'], y=point.data['long']))
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
