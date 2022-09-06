from django.contrib.gis import admin
from leaflet.admin import LeafletGeoAdmin
from .models import Houses

# Register your models here.

@admin.register(Houses)

class HousesAdmin(LeafletGeoAdmin):
    list_display = ('name', 'location')