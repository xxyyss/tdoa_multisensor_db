"""tdoa_multisensor_db URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from interface import views

router = routers.DefaultRouter()
router.register(r'positions', views.PositionViewSet)
router.register(r'sensors', views.SensorViewSet)
router.register(r'sound_sources', views.SoundSourceViewSet)
router.register(r'worlds', views.WorldViewSet)

# router.register(r'world_related', views.WorldRelatedViewSet)
router.register(r'network_adapters', views.NetworkAdapterViewSet)
# router.register(r'has_network_adapters', views.HasNetworkAdapterViewSet) abstract
router.register(r'int_bounds', views.IntBoundViewSet)

router.register(r'int_intervals', views.IntIntervalViewSet)
router.register(r'network_connections', views.NetworkConnectionViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls))
]


# (Position, Sensor, SoundSource, World, WorldRelated, NetworkAdapter, HasNetworkAdapter, IntBound,
#                      IntInterval, NetworkConnection)
