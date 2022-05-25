from django.contrib import admin

from home.models import Settings, ContactFormMessage, UserProfile


class SettingsAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter = ['status']


class ContactFormMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'message', 'note', 'status']
    list_filter = ['status']


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'phone', 'address', 'city', 'country', 'image_tag']


admin.site.register(Settings, SettingsAdmin)
admin.site.register(ContactFormMessage, ContactFormMessageAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
