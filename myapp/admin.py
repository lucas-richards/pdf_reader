from django.contrib import admin

# Register your models here.
from .models import Client, Invoice

admin.site.register(Client)
admin.site.register(Invoice)
