from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'provider', views.ProviderViewSet, basename="providers")
router.register(r'geopolygon', views.GeoPolygonViewSet, basename="geopolygons")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('polygon/get/', views.get_polygon, name='get_polygon'),

]
