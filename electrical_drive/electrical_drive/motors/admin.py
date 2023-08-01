from django.contrib import admin

from electrical_drive.motors.models import Bikes

# admin.site.register(Bikes)


@admin.register(Bikes)
class BikesAdmin(admin.ModelAdmin):
    list_filter = ('price',)
    search_fields = ('brand',)
