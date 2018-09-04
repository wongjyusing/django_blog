from django.contrib import admin
from .models import Blog
# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','slug', 'author', 'created_time', 'update_time')
