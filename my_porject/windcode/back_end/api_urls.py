from django.urls import path,re_path
from . import api_views
urlpatterns = [

    path('',api_views.blog_list),
    path('basedata/',api_views.toolbox),
    re_path('detail/(?P<slug>[\w-]+)/', api_views.blog_detail, name='detail'),
    re_path('blog_tag/(?P<slug>[\w-]+)/', api_views.blog_tag, name='tag'),
]
