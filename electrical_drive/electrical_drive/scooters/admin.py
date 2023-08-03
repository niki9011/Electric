from django.contrib import admin

from .models import Scooters


@admin.register(Scooters)
class ScootersAdmin(admin.ModelAdmin):
    list_filter = ('price',)
    search_fields = ('brand',)
