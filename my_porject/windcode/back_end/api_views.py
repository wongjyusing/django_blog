from django.http import JsonResponse
from django.core import serializers
import json
import markdown
from .blog import models as BlogModel
from .book import models as BookModel
from .toolbox import models as ToolBox

def toolbox(request):
    context = {}
    try:
        blog_tag = BlogModel.BlogTag.objects.all()
        toolbox = ToolBox.ToolParameter.objects.all()
        mysite = ToolBox.MySite.objects.all()
        context['data_type'] = 'toolbox'
        context['blog_tag'] = json.loads(serializers.serialize("json", blog_tag))
        context['toolbox'] = json.loads(serializers.serialize("json", toolbox))
        context['mysite'] = json.loads(serializers.serialize("json", mysite))
    except Exception as e:

        context['msg'] = 'ERROR'


    return JsonResponse(context,json_dumps_params={'ensure_ascii':False})



def blog_list(request):
    context = {}
    try:
        context['data_type'] = 'blog_list'
        blog = BlogModel.Blog.objects.all()
        context['blogs'] = json.loads(serializers.serialize("json", blog))
        context['msg'] = 'success'

    except Exception as e:

        context['msg'] = 'ERROR'


    return JsonResponse(context,json_dumps_params={'ensure_ascii':False})


def blog_tag(request,slug):
    context = {}
    try:
        blog_tag = BlogModel.BlogTag.objects.get(slug=slug)
        blog = BlogModel.Blog.objects.filter(blog_tag=blog_tag)
        context['blog'] = json.loads(serializers.serialize("json", blog))
    except Exception as e:
        context['msg'] = 'ERROR'


    return JsonResponse(context,json_dumps_params={'ensure_ascii':False})


def blog_detail(request,slug):
    context = {}
    try:
        blog = BlogModel.Blog.objects.filter(slug=slug)


        blog_data = BlogModel.Blog.objects.get(slug=slug)
        context['blog'] = json.loads(serializers.serialize("json", blog))

        context['markdown'] = markdown.markdown(blog_data.body,
                                     extensions=[
                                         'markdown.extensions.extra',
                                         'markdown.extensions.codehilite',
                                         'markdown.extensions.toc',
                                     ])

    except Exception as e:
        context['msg'] = 'ERROR'


    return JsonResponse(context,json_dumps_params={'ensure_ascii':False})




'''
# 博客列表页
def blog_list(request):
    context = {}
    try:
        # 获取博客的所有对象
        blog = BlogModel.Blog.objects.all()
        # 通用信息获取，包括博客的标题、个人中心、友情链接、书本链接、等通用信息
        toolbox = ToolBox.ToolParameter.objects.all()
        # 让前端知道数据获取成功
        context['msg'] = 'success'
        # 让前端知道匹配那种处理方法
        context['data_type'] = 'blog_list'
        # 对获取的数据进行格式化处理
        context['toolbox'] = json.loads(serializers.serialize("json", toolbox))
        context['blogs'] = json.loads(serializers.serialize("json", blog))
    except Exception as e:
        context['msg'] = 'error'

    return JsonResponse(context,json_dumps_params={'ensure_ascii':False})
'''
