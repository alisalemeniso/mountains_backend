import geopandas as gpd
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from shapely import geometry

from mountains.models import Mountain
from mountains.serializers import MountainsSerializer


class MountainsViewSet(viewsets.ModelViewSet):
    serializer_class = MountainsSerializer
    queryset = Mountain.objects.all()

    def perform_create(self, serializer):
        x = 0
        latitude = serializer.validated_data['lat']
        longitude = serializer.validated_data['long']
        point = 'POINT(' + str(longitude) + ' ' + str(latitude) + ')'
        serializer.save(location=point)

    @action(url_path="peaks_within", methods=["post"], detail=False)
    def report_post(self, request, *args, **kwargs):
        try:
            crs = {'init': 'epsg:4326'}
            query = Mountain.objects.all()
            x1 = request.data['x1']
            x2 = request.data['x2']
            y1 = request.data['y1']
            y2 = request.data['y2']
            pointList = [(39.77750000, 116.17944444), (39.77750000, 116.58888889), (40.04722222, 116.58888889),
                         (40.04722222, 116.17944444)]
            # pointList=[(x1,y1), (x1,y2), (x2,y1), (x2,y2)]
            poly = geometry.Polygon(pointList)
            spoly = gpd.GeoSeries([poly], crs=crs)
            list_peaks = Mountain.objects.all()
            geodataframe = [geometry.Point(xy) for xy in zip(query.lat, query.long)]

            pass
            return Response({"message": "this is a result"})
        except Exception as e:
            return Response({"err": str(e)})

    @action(url_path="test", methods=["get"], detail=False)
    def test_func(self, request, *args, **kwargs):
        try:
            # x1 = request.data['x1']
            # x2 = request.data['x2']
            # y1 = request.data['y1']
            # y2 = request.data['y2']
            pointList = [(39.77750000, 116.17944444), (39.77750000, 116.58888889), (40.04722222, 116.58888889),
                         (40.04722222, 116.17944444)]
            # pointList=[(x1,y1), (x1,y2), (x2,y1), (x2,y2)]
            poly = geometry.Polygon(pointList)
            peaks = Mountain.objects.first(location__within=poly)

            pass
            return Response({"message": "this is a result"})
        except Exception as e:
            return Response({"err": str(e)})
