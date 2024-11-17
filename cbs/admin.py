from django.contrib import admin
from cbs.models import Record, User
from cbs.admin_package import RecordAdmin
from cbs.admin_package import UserAdmin 

admin.site.register(Record, RecordAdmin)
admin.site.register(User, UserAdmin)