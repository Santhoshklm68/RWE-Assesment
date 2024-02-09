from rest_framework import serializers
from rpm_service.models.DeviceProvider import DeviceProviderModel

class Deviceproviderserializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceProviderModel
        fields = ["name","enabled"]