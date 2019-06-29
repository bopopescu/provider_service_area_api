import pycountry
from phone_field import PhoneField
from django.db import models

from provider_service_area_api.models_util import BaseModel


LANGUAGES = [(lang.alpha_3, lang.name) for lang in sorted(pycountry.languages, key=lambda x: x.name)]

CURRENCIES = [(cur.alpha_3, cur.name) for cur in sorted(pycountry.currencies, key=lambda x: x.name)]


class Provider(BaseModel):
    """ Model to store Transportation providers """

    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254, unique=True)  # #RFCs 3696
    phone_number = PhoneField(help_text='Contact phone number')
    language = models.CharField(max_length=3, choices=LANGUAGES)  # #ISO 639
    currency = models.CharField(max_length=3, choices=CURRENCIES)  # #ISO 4217

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name
