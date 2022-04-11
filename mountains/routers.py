from rest_framework import routers

from mountains.views import MountainsViewSet

peaks_router = routers.DefaultRouter()
peaks_router.register('', MountainsViewSet)
