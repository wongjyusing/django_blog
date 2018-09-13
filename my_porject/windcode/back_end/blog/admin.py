from django.contrib import admin
from .models import Blog, BlogTag
# Register your models here.

@admin.register(BlogTag)
class BlogTagAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'slug','body')


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'slug', 'author', 'created_time', 'update_time')
