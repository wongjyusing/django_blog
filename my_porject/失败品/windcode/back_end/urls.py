from django.urls import path,re_path
from .books import views as book_views
urlpatterns = [
    path('api/',book_views.book_list),
    re_path('api_chapter/(?P<slug>[\w-]+)/',book_views.book_chapter)
]
