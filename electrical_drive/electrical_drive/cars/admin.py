from django.contrib import admin

from electrical_drive.cars.models import Cars


@admin.register(Cars)
class CarsAdmin(admin.ModelAdmin):
    list_filter = ('price',)
    search_fields = ('brand',)
