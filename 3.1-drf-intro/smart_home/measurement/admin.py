from django.contrib import admin

from .models import Sensor, Measurement


@admin.register(Sensor,Measurement)
class CarAdmin(admin.ModelAdmin):
    pass
