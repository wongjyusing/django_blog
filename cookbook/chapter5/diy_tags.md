## 什么是自定义模板标签？
其实问你**什么是xxxxx？**  
把问题转化成**为什么要使用自定义模板标签？**  
学习的动力就来了。  
结合这个项目来说，现在有个需求。  
需要在**博客列表页**的右半部分显示我们的**所有标签的列表**。  
按照我们前面的写法，做不到，显示不出来（利用模板语言在**所有博客列表页**可以做到，但很麻烦，其他页面肯定不行）  
如果要显示的话，需要把views.py中的blog_list函数改写成下面的样式。  
```python
def blog_list(request):
    context = {}

    contact_list = Blog.objects.all()
    # 从请求中查找是否有page参数，如果有则取page的参数
    # 没有则取1
    page = request.GET.get('page',1)

    context['blogs'] = page_gen(contact_list,page)

    context['blog_tag'] = BlogTag.objects.all()

    return render(request, 'blog_list.html', context)
```
现在再来个需求、要在**首页**显示所有的标签和类型又要改写home函数，如下:
```python
def home(request):
    context = {}
    context['blog_tag'] = BlogTag.objects.all()
    context['blog_type'] = BlogType.objects.all()
    return render(request,'home.html',context)
```
需求又双叒叕来了。  
那样就会导致我们的views.py的代码变得超样衰。  
自定义模板标签可以帮我们解决这个问题。  
现在有了学习的动力了吧？？  
## 创建你的第一个自定义模板标签  
把终端切换到项目根目录下，依次输入以下代码
```python
mkdir apps/blog/templatetags

touch apps/blog/templatetags/__init__.py

touch apps/blog/templatetags/diy_tags.py

```
`templatetags`这个目录名不能修改，系统默认的。  
`__init__.py`这个文件是声明templatetags是一个python包  
`diy_tags.py`是我们编写自定义模板标签的文件。  
刚才上面说了要在**博客列表页**显示我们**所有的标签列表对吧？？**  
要在要在**首页**显示所有的**标签和类型**列表对吧？？？
## diy_tags.py
```python
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
    # 下面的代码意思是
    # 通常很多人把博客部署上线后，都会列一大堆标签、分类等（例如我）
    # 心中总有个大计划，要写Django、Tornado、Requests、
    # Scrapy、Flask、Linux、MongoDB、MySQL、Vue
    # 但又迟迟不更新。很多标签或类型下是没有文章的
    # 简单来说，如果该标签或者分类下没有文章，则不返回该标签或分类
    return BlogType.objects.annotate(total_num=Count('blog')).filter(total_num__gt=0)




@register.simple_tag
def get_detail_tags(each):
    tags = Blog.blog_tag
    return tags

```
好了写完了自定义模板标签。  
该怎么用呢？？
例如说要在首页显示该内容。  
首页的模板文件是home.html。  
注意阅读里面的注释如下：  
```html
<!DOCTYPE html>
{% load diy_tags %}   {# 导入我们的自定义模板标签 #}
<html lang="en" dir="ltr">
    <head>
        <meta charset="utf-8">
        <title>首页</title>
    </head>
    <body>
        <div class="site-me-widget-first">
            <h4 class="title">标签</h4>
            <hr>
            <div class="content community">
                {% get_blog_tag_list as tag_list %}  {# 把函数实例化为变量名 #}
                {% for tag in tag_list %}     {# 通过for循环遍历出内容 #}
                    <li class="blog-type-tag"><a target="_blank" href="{% url 'blog_tag' tag.slug %}">{{ tag.name }}</a></li>
                {% empty %}   {# 这个empty是说，假如没有标签的话，显示下面p标签的内容 #}
                    <p>暂无标签 敬请期待</p>
                {% endfor %}
            </div>
            <div class="content community">
                {% get_blog_type_list as type_list %}  {# 把函数实例化为变量名 #}
                {% for type in type_list %}     {# 通过for循环遍历出内容 #}
                    <li class="blog-type-tag"><a target="_blank" href="{% url 'blog_type' type.slug %}">{{ type.name }}</a></li>
                {% empty %}   {# 这个empty是说，假如没有标签的话，显示下面p标签的内容 #}
                    <p>暂无分类 敬请期待</p>
                {% endfor %}
            </div>
        </div>
    </body>
</html>
```
那么需求不管它怎么来，我们都可以从容应对，这就是自定义模板标签。  
其实自定义模板还可以应用到搜索方面去哦。大家自己写个函数试试。  
因为它可以做到在模板上传参。  
下一篇介绍**模板拓展方法**。  
还是那句话，先不要敲代码。  
最后会总结开发的思路。回头再研究代码。
