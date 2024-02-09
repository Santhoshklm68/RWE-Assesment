from rest_framework import serializers
from rpm_service.models.ConnectivityType import ConnectivityTypeModel

class Connectivityserializer(serializers.ModelSerializer):
    class Meta:
        model = ConnectivityTypeModel
        fields = ["name", "description"] 