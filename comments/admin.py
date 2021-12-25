from django.contrib import admin
from .models import *
# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    model = Comment
    list_display = ('name', 'email', 'created_time')
    list_filter = ('name', 'email', 'created_time')

admin.site.register(Comment, CommentAdmin)