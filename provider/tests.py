import json

from django.test import TestCase
from rest_framework.reverse import reverse

from provider.models import Provider
from provider.serializer import ProviderSerializer


class ProviderViewSetTest(TestCase):
    """
    Test case for all Provider ViewSets
    """

    def setUp(self):
        self.provider_sample = Provider.objects.create(name='Ankit Arora',
                                                       email='ankit@gmail.com',
                                                       phone_number='+919892122165',
                                                       language='hin',
                                                       currency='INR')

    def test_provider_list(self):
        """
        Provider List endpoint
        """
        resp = self.client.get(reverse("providers-list"))
        self.assertEqual(dict(resp.data['results'][0]),
                         ProviderSerializer(self.provider_sample).data)

    def test_provider_create(self):
        """
        Should create/post a provider and return the provider
        """
        resp = self.client.post(
            reverse('providers-list'),
            data={'currency': 'USD',
                  'email': 'ankit2@gmail.com',
                  'language': 'eng',
                  'name': 'Ankit 2',
                  'phone_number': '+919876543210'})
        self.assertEqual(resp.data,
                         ProviderSerializer(instance=Provider.objects.last()).data)

    def test_provider_remove(self):
        """
        Should delete a provider
        """
        resp = self.client.delete(reverse('providers-detail', kwargs={'pk': self.provider_sample.pk}))
        self.assertIsNone(resp.data)
        self.assertEqual(list(Provider.objects.filter(pk=self.provider_sample.pk)), [])

    def test_provider_partial_update(self):
        """
        Should let update a provider
        """
        resp = self.client.patch(reverse('providers-detail',
                                         kwargs={'pk': self.provider_sample.pk}),
                                 data=json.dumps({'name': 'Ankit 3'}),
                                 content_type="application/json")
        self.assertEqual(resp.data['name'], 'Ankit 3')

    def test_provider_fetch(self):
        """
        Should fetch a provider
        """
        resp = self.client.get(reverse('providers-detail',
                                       kwargs={'pk': self.provider_sample.pk}))
        self.assertEqual(resp.data,
                         ProviderSerializer(self.provider_sample).data)

    def test_provider_update(self):
        """
        Should update a provider
        """
        data = ProviderSerializer(self.provider_sample).data
        data['name'] = 'Ankit 4'
        resp = self.client.put(reverse('providers-detail',
                                       kwargs={'pk': self.provider_sample.pk}),
                               data=json.dumps(data),
                               content_type="application/json")
        self.assertEqual(resp.data, data)
