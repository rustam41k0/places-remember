from django.contrib.gis import admin
from .models import Memory


@admin.register(Memory)
class MemoryAdmin(admin.OSMGeoAdmin):
    list_display = ("title", "location")
