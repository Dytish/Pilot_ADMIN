from cbs.serializers.serializers import FlexibleModelSerializer
from cbs.models.record import Record


class RecordSerializer(FlexibleModelSerializer):
    class Meta:
        model = Record
        fields = '__all__' 