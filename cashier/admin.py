from django.contrib import admin
from .models import Products , Sales , Purchases

# Register your models here.

admin.site.register(Products)
admin.site.register(Sales)
admin.site.register(Purchases)
