from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from cbs.models.location import City, District, Region
from cbs.serializers.location import DistrictSerializer, RegionSerializer, CitySerializer


class DistrictViewSet(viewsets.ModelViewSet):
    queryset = District.objects.all()
    permission_classes = [AllowAny]
    serializer_class = DistrictSerializer


class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegionSerializer

    @action(detail=False, methods=['get'], url_path='by-district')
    def get_by_district(self, request):
        """
        Получение всех регионов по конкретной области (district).
        """
        district_id = request.query_params.get('district_id')
        if not district_id:
            return Response({"error": "Параметр 'district_id' обязателен."}, status=400)
        try:
            district_id = int(district_id)
            regions = Region.objects.filter(district_id=district_id)
            if not regions.exists():
                return Response({"message": "Регионы не найдены для указанного округа."}, status=404)
            serializer = self.get_serializer(regions, many=True)
            return Response(serializer.data, status=200)
        except ValueError:
            return Response({"error": "Параметр 'district_id' должен быть целым числом."}, status=400)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
        

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    permission_classes = [AllowAny]
    serializer_class = CitySerializer

    @action(detail=False, methods=['get'], url_path='by-region')
    def get_by_region(self, request):
        """
        Получение всех городов по конкретному региону (region).
        """
        region_id = request.query_params.get('region_id')
        if not region_id:
            return Response({"error": "Параметр 'region_id' обязателен."}, status=400)
        try:
            region_id = int(region_id)
            cities = City.objects.filter(region_id=region_id)
            if not cities.exists():
                return Response({"message": "Города не найдены для указанного региона."}, status=404)
            serializer = self.get_serializer(cities, many=True)
            return Response(serializer.data, status=200)
        except ValueError:
            return Response({"error": "Параметр 'region_id' должен быть целым числом."}, status=400)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
