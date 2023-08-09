from django.contrib import admin
from electrical_drive.news.models import AllNews


@admin.register(AllNews)
class AllNewsAdmin(admin.ModelAdmin):
    list_filter = ('data',)
    search_fields = ('subject',)
