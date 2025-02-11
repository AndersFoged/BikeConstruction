from django.contrib import admin
from .models import BikeModelBike, BikeType  # Make sure names match models.py

admin.site.register(BikeType)
admin.site.register(BikeModelBike)
