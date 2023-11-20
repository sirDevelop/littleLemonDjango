from django.contrib import admin
from .models import DeliveryCrew, Manager

# Register your models here.

admin.site.register(Manager)
admin.site.register(DeliveryCrew)
# admin.site.register(Genre)