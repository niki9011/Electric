from django.contrib import admin
from electrical_drive.news.models import Allnews


@admin.register(Allnews)
class AllnewsAdmin(admin.ModelAdmin):
    list_filter = ('data',)
    search_fields = ('subject',)
