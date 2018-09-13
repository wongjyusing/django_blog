from django.contrib import admin
from .models import Book,Chapter,Section
# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug','status_models', 'author', 'created_time', 'update_time')



@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug','page_num', 'book_name',)

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug','page_num', 'chaptet',)
