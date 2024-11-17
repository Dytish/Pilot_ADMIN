from cbs.serializers.serializers import FlexibleModelSerializer
from cbs.models.user import User


class UserSerializer(FlexibleModelSerializer):
    class Meta:
        model = User
        fields = '__all__' 