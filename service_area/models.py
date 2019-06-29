from django.db import models
from django.contrib.gis.db import models as geomodels

from provider_service_area_api.models_util import BaseModel
from provider.models import Provider


class ServiceArea(BaseModel):
    """
    Model to store the name, service area and price of transport providers
    """
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, related_name='service_areas')

    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    polygons = geomodels.MultiPolygonField(spatial_index=True)

    @property
    def provider_name(self):
        return self.provider.name

    class Meta:
        ordering = ['-created']
