from rest_framework import serializers
from rpm_service.models.Device import DeviceModel

class Deviceserializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceModel
        fields = ["external_id", "name", "description", "type", "model", "manufactured_by", "connectivity_type", "device_provider", "uuid","organization_id", "rental_cost", "buy_cost", "image_url"]