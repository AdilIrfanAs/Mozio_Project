from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from shapely.geometry import Polygon, Point

from .models import GeoPolygon, Provider
from .serializers import GeoSerializer, ProviderSerializer,QuerySerializer


class ProviderViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    """
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer


class GeoPolygonViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    """
    queryset = GeoPolygon.objects.all()
    serializer_class = GeoSerializer
    http_method_names = ['post', 'put', 'patch', 'delete', 'get']


@api_view(['GET'])
def get_polygon(request):
    """
    get_polygon function outputs the all the polygon information associated with
    a particular latitude and longtitude
    Gets lat (latitude) and long (longitude) from the URL query parameters
    Selects Polygons that contain latitude and longitude
    Returns a polygon which is serialised by QuerySerializer
    """
    lat = request.GET.get('lat', None)
    long = request.GET.get('long', None)

    if lat is None or long is None:
        return Response('ploygon does not exist against this latitude and longitude')

    point = Point(float(lat), float(long))
    selected_poly = []
    queryset = GeoPolygon.objects.filter(poly=point)
    for polygons in queryset:
        poly_coord = polygons.poly
        eval_poly_coord = eval(poly_coord)
        polygon = Polygon(eval_poly_coord)
        if polygon.contains(point):
            selected_poly.append(polygons)

    if not selected_poly:
        return Response('No Provider available')

    serializer = QuerySerializer(selected_poly, many=True)
    return Response(serializer.data)
