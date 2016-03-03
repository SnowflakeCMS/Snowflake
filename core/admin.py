from django.contrib import admin

# Register your models here.

from core.models import Setting, Blog

admin.site.register(Setting)
admin.site.register(Blog)