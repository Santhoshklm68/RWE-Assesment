from rpm_service.serializers.connectivityserializer import Connectivityserializer
from rest_framework import viewsets
from rpm_service.models import ConnectivityTypeModel

class ConnectivityTypeViewSet(viewsets.ModelViewSet):
    queryset = ConnectivityTypeModel.objects.all()
    serializer_class = Connectivityserializer