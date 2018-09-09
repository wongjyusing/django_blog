# pork_suimai/apps/blog/templaatetags/diy_tags
from django import template     # 从Django中导入模板方法
from ..models import BlogTag,Blog,BlogType
from django.db.models.aggregates import Count   # 从django的数据库模型总数中导入计数方法
register = template.Library()   # 注册   模板的库   Library 图书馆，可以理解为放书进去，

@register.simple_tag
def test(): # 测试
    return 'hello world'

@register.simple_tag    # 注册简单标签，这是python关于装饰器的方法
def get_blog_list():# 获取所有博客列表
    return Blog.objects.all()


@register.simple_tag
def get_blog_tag_list(): # 获取博客标签列表
    return BlogTag.objects.annotate(total_num=Count('blog')).filter(total_num__gt=0)

@register.simple_tag
def get_blog_type_list(): # 获取博客标签列表
    return BlogType.objects.annotate(total_num=Count('blog')).filter(total_num__gt=0)




@register.simple_tag
def get_detail_tags(each):
    tags = Blog.blog_tag
    return tags
