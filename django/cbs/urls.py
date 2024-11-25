from rest_framework import routers
from cbs.api.record import RecordViewSet
from cbs.api.user import UserViewSet
from cbs.api.location import RegionViewSet, DistrictViewSet, CityViewSet


router = routers.DefaultRouter()
router.register('api/user', UserViewSet, 'user')
router.register('api/record', RecordViewSet, 'record')
router.register('api/location/district', DistrictViewSet, 'district')
router.register('api/location/region', RegionViewSet, 'region')
router.register('api/location/city', CityViewSet, 'city')


urlpatterns = router.urls


# router.register('api/record', RecordViewSet, 'record')
# # router.urls
# urlpatterns = [ 
#     path('api/user/<int:user_tg_id>/', UserViewSet.as_view(), name='user-detail'),
# ]