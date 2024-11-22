from cbs.serializers.serializers import FlexibleModelSerializer
from cbs.models.location import City, District, Region


class CitySerializer(FlexibleModelSerializer):
    class Meta:
        model = City
        fields = '__all__' 

class DistrictSerializer(FlexibleModelSerializer):
    class Meta:
        model = District
        fields = '__all__' 

class RegionSerializer(FlexibleModelSerializer):
    class Meta:
        model = Region
        fields = '__all__' 