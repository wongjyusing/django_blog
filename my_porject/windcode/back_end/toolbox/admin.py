from django.contrib import admin
from .models import ToolName, ToolParameter,MySite
# Register your models here.

@admin.register(ToolName)
class ToolNameAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'slug',)


@admin.register(ToolParameter)
class ToolParameterAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'link', 'img_link', 'introduction', 'tool_name')

@admin.register(MySite)
class MySiteAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'introduction', 'powered','approval_number')
