from django.contrib.gis import admin
from .models import TriFacility, TriRelease, DmrFacility, DmrRelease

# Register your models here.
admin.site.register(TriFacility, admin.OSMGeoAdmin)
admin.site.register(TriRelease, admin.OSMGeoAdmin)
admin.site.register(DmrFacility, admin.OSMGeoAdmin)
admin.site.register(DmrRelease, admin.OSMGeoAdmin)
