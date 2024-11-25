from django.contrib import admin


class DistrictAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    ordering = ('name',)

class RegionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'district')
    list_filter = ('district',)
    search_fields = ('name', 'district__name')
    ordering = ('district', 'name')

class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'region')
    list_filter = ('region',)
    search_fields = ('name', 'region__name', 'region__district__name')
    ordering = ('region', 'name')
