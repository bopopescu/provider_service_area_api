import json

from django.contrib.gis.geos import Polygon, MultiPolygon
from django.test import TestCase
from rest_framework.reverse import reverse

from provider.models import Provider
from service_area.models import ServiceArea
from service_area.serializer import ServiceAreaSerializer


class ServiceAreaViewSetTest(TestCase):
    """
    Test case for all ServiceArea ViewSets
    """

    def setUp(self):
        self.provider_sample = Provider.objects.create(name='Ankit Arora',
                                                       email='ankit@gmail.com',
                                                       phone_number='+919892122165',
                                                       language='hin',
                                                       currency='INR')
        self.service_area = ServiceArea.objects.create(provider=self.provider_sample,
                                                       name='Some Area',
                                                       price='200.00',
                                                       polygons=MultiPolygon(Polygon(((0, 0), (0, 1), (1, 1), (0, 0))),
                                                                             Polygon(((1, 1), (1, 2), (2, 2), (1, 1)))))

    def test_service_areas_list(self):
        """
        ServiceArea list endpoint
        """
        resp = self.client.get(reverse('service-areas-list'))
        self.assertEqual(
            dict(resp.data['results']['features'][0]),
            ServiceAreaSerializer(self.service_area).data)

    def test_service_areas_create(self):
        """
        Should create/post a service_area and return the service_area
        """
        data = {'provider': self.provider_sample.pk,
                'name': 'Some Area',
                'price': '200.00',
                'polygons': {
                    'coordinates': [[[[0.0, 0.0], [0.0, 1.0], [1.0, 1.0], [0.0, 0.0]]],
                                    [[[1.0, 1.0], [1.0, 2.0], [1.0, 2.0], [1.0, 1.0]]]],
                    'type': 'MultiPolygon'}}
        resp = self.client.post(reverse('service-areas-list'),
                                data=json.dumps(data),
                                content_type="application/json")
        self.assertEqual(resp.data,
                         ServiceAreaSerializer(instance=ServiceArea.objects.latest('created')).data)

    def test_service_areas_find(self):
        """
        Fetch an area by lat & long params
        """
        resp = self.client.get(reverse('service-areas-find'),
                               data={'lat': 0.5, 'long': 0.5})
        self.assertEqual(dict(resp.data['features'][0]),
                         ServiceAreaSerializer(self.service_area).data)
        self.assertEqual(len(resp.data['features']), 1)
