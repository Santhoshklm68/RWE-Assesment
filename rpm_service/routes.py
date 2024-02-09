from rest_framework.routers import DefaultRouter

from rpm_service.views.connectivity import ConnectivityTypeViewSet
from rpm_service.views.device import DeviceViewSet
from rpm_service.views.deviceprovider import DeviceProviderViewSet

router = DefaultRouter()


router.register(
    "connectivity-type", 
    ConnectivityTypeViewSet, 
    basename="connectivity_type"
)
router.register(
    "device",
    DeviceViewSet,
    basename="device"
)


router.register(
    "device-provider",
    DeviceProviderViewSet,
    basename="device_provider"
)
