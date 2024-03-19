from django.contrib import admin
from .models import labels,Notification, Facultie
# Register your models here.

admin.site.register(labels)
admin.site.register(Notification)
admin.site.register(Facultie)