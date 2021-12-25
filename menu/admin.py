from django.contrib import admin

# Register your models here.

from .models import  MenuItem, Menu
from django.contrib import admin

admin.site.register(Menu)
admin.site.register(MenuItem)