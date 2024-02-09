from rpm_service.serializers.deviceprovider import Deviceproviderserializer
from rest_framework import viewsets
from rpm_service.models.DeviceProvider import DeviceProviderModel

class DeviceProviderViewSet(viewsets.ModelViewSet):
    queryset = DeviceProviderModel.objects.all()
    serializer_class = Deviceproviderserializer