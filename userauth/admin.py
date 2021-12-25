from django.contrib import admin
from .models import Code, CustomUser
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Code)