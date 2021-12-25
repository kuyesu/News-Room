from django.contrib import admin
from .models import *
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    model = Contact
    list_display = ('name', 'email', 'subject')
    list_filter = ('name', 'email', 'subject')

class AboutAdmin(admin.ModelAdmin):
    model = About
    
    list_filter = ('title',)


admin.site.register(Contact, ContactAdmin)
admin.site.register(About, AboutAdmin)