from django.urls import path,re_path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('blog_list/', views.blog_list, name='blog_list'),
    re_path('type/(?P<slug>[\w-]+)/', views.blog_tag, name='blog_type'),
    re_path('tag/(?P<slug>[\w-]+)/', views.blog_tag, name='blog_tag'),
    re_path('detail/(?P<slug>[\w-]+)/', views.blog_detail, name='detail'),
    
]
