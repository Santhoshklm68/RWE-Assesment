from rest_framework import viewsets
from rpm_service.models.Device import DeviceModel
from rpm_service.serializers.deviceserializer import Deviceserializer



class DeviceViewSet(viewsets.ModelViewSet):
    queryset = DeviceModel.objects.all()
    serializer_class = Deviceserializer