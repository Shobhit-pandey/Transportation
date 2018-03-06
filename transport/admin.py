from django.contrib import admin

# Register your models here.
from transport.models import TruckLists

admin.site.site_header = "Internship Project"


admin.site.register(TruckLists)