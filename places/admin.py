from django.contrib.gis import admin
from leaflet.admin import LeafletGeoAdmin
from .models import Myplaces

# Register your models here.

@admin.register(Myplaces)

class MyplacesAdmin(LeafletGeoAdmin):
    list_display = ('name', 'location')