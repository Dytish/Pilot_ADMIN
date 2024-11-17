from rest_framework import routers
from cbs.api.record import RecordViewSet
from cbs.api.user import UserViewSet


router = routers.DefaultRouter()
router.register('api/user', UserViewSet, 'user')
router.register('api/record', RecordViewSet, 'record')

urlpatterns = router.urls


# router.register('api/record', RecordViewSet, 'record')
# # router.urls
# urlpatterns = [ 
#     path('api/user/<int:user_tg_id>/', UserViewSet.as_view(), name='user-detail'),
# ]