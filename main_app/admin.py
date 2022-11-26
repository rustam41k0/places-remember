from django.contrib import admin
from django.contrib.gis import admin
from .models import Memory


# admin.site.register(Memory)
@admin.register(Memory)
class MemoryAdmin(admin.OSMGeoAdmin):
    list_display = ("title", "location")
