# import geopandas as gpd
from rest_framework import viewsets
# from rest_framework.decorators import action
# from rest_framework.response import Response
# from shapely import geometry

from mountains.models import Mountain
from mountains.serializers import MountainsSerializer


class MountainsViewSet(viewsets.ModelViewSet):
    serializer_class = MountainsSerializer
    queryset = Mountain.objects.all()

    # def perform_create(self, serializer):
    #     x = 0
    #     latitude = serializer.validated_data['lat']
    #     longitude = serializer.validated_data['long']
    #     point = 'POINT(' + str(longitude) + ' ' + str(latitude) + ')'
    #     serializer.save(location=point)


    # @action(url_path="peaks_box", methods=["post"], detail=False)
    # def peaks_in_box(self, request, *args, **kwargs):
    #     try:
    #         # x1 = request.data['x1']
    #         # x2 = request.data['x2']
    #         # y1 = request.data['y1']
    #         # y2 = request.data['y2']
    #         pointList = [(39.77750000, 116.17944444), (39.77750000, 116.58888889), (40.04722222, 116.58888889),
    #                      (40.04722222, 116.17944444)]
    #         # pointList=[(x1,y1), (x1,y2), (x2,y1), (x2,y2)]
    #         poly = geometry.Polygon(pointList)
    #         peaks = Mountain.objects.first(location__within=poly)
    #
    #         pass
    #         return Response({"message": "this is a result"})
    #     except Exception as e:
    #         return Response({"err": str(e)})
