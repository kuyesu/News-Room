from django.contrib import admin
from .models import *
# Register your models here.



class LinkAdmin(admin.ModelAdmin):
    model = Link
    list_display = ('name', 'url')
    list_filter = ('name', 'url')

class SocialAdmin(admin.ModelAdmin):
    model = Social
    list_display = ('name', 'url')
    list_filter = ('name', 'url')

admin.site.register(Link, LinkAdmin)
admin.site.register(Social, SocialAdmin)
admin.site.register(AdvertisementBanner)
admin.site.register(SiteName)
admin.site.register(LogoImage)