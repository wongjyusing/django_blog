from django.urls import path,re_path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('blog_list',views.blog_list,name='blog_list'),
]
