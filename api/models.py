from django.contrib.gis.db import models

LANGUAGE_CHOICES = [
    ('ENG', 'English'),
    ('SPA', 'Spanish'),
    ('CHI', 'Chinese'),
    ('FRA', 'French'),
    ('GER', 'German'),
    ('HIN', 'Hindi'),
    ('JPN', 'Japanese'),
    ('AR', 'Arabic'),
]

CURRENCY_CHOICES = [
    ('USD', 'US Dollar'),
    ('JPY', 'Japanese Yen'),
    ('CNY', 'Chinese Yuan'),
    ('INR', 'Indian Rupee'),
    ('EUR', 'Euro'),
    ('GBP', 'Pound'),
]


class Provider(models.Model):
    """
    The Provider class defines the data storage for each provider
    It has the following fields:
    name -> Character field to store the name of the provider
    email -> email field to store the email of the provider
    phonenumber -> Big integer field to store the phone number
    language -> Character field to choose the languages from LANGUAGE_CHOICES
    currency -> Character field to choose the currency from CURRENCY_CHOICES
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.BigIntegerField()
    language = models.CharField(max_length=3, choices=LANGUAGE_CHOICES)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES)

    def __str__(self):
        return self.name


class GeoPolygon(models.Model):
    """
    The GeoPolygon class defines the data storage for each polygon
    It has the following fields:
    provider -> It acts a foriegn key to Provider class allowing One to Many Relationships
                So each Provider can have multiple GeoPolygon objects
    price -> Decimal Field to allow price to be set for each polygon
    poly -> Polygon Field to allow dimensions of the polygon to be set
    """
    provider = models.ForeignKey('Provider', on_delete=models.CASCADE)
    polygon_name = models.CharField(max_length=256, default='newpoly')
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    poly = models.PolygonField()

    def __str__(self):
        return self.polygon_name
