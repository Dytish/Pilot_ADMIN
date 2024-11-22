from django.contrib import admin
from cbs.models import Record, User, City, Region, District
from cbs.admin_package import RecordAdmin
from cbs.admin_package import UserAdmin 
from cbs.admin_package import DistrictAdmin, RegionAdmin, CityAdmin 


admin.site.register(Record, RecordAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(District, DistrictAdmin)