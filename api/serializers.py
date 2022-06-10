from api.models import Provider, GeoPolygon
from rest_framework import serializers


class ProviderSerializer(serializers.ModelSerializer):
    """
    ProviderSerializer class is used for serializing the Provider class
    It outputs all the fields associated with the model Provider
    """

    class Meta:
        model = Provider
        fields = ['name', 'email', 'phone_number',
                  'phone_number', 'language', 'currency']


class GeoSerializer(serializers.ModelSerializer):
    """
    GeoSerializer class is used for serializing the GeoPolygon class
    It contains all the fields associated with the GeoPolygon model

    """

    class Meta:
        model = GeoPolygon
        fields = ['provider', 'polygon_name', 'price', 'poly']


class QuerySerializer(serializers.ModelSerializer):
    """
    QuerySerializer class is used for showing the query polygon to the Users
    It removes the poly field to remove the dimensions of the polygon
    """

    class Meta:
        model = GeoPolygon
        fields = ['provider', 'polygon_name', 'price']
