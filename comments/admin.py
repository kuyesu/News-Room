from django.contrib import admin
from .models import *
# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    model = Comment
    list_display = ('user', 'email', 'created_time')
    list_filter = ('user', 'email', 'created_time')

admin.site.register(Comment, CommentAdmin)


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0