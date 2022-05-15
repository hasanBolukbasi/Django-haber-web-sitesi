from django.contrib import admin

from home.models import Settings


class SettingsAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter = ['status']


admin.site.register(Settings, SettingsAdmin)