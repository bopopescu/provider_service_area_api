from rest_framework import viewsets
from provider.serializer import ProviderSerializer
from provider.models import Provider


class ProviderViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Providers
    """

    queryset = Provider.objects.order_by('-created')
    serializer_class = ProviderSerializer
    partial = True
