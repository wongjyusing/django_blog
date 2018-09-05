## 说明  
大家最好把之前做的项目基本配置复制一份到另外的目录下。  
也可以每次新建项目都重新配置一次。  
因为后续会分几种类型的博客进行搭建。  
有以**分类、标签、书结构**等博客类型。  
最后还会有动态网页型的博客。  
这次教程完成后，我的博客也会进行升级。  
***
希望大家忘了之前的例子，现在重新做一个。  
因为可以让你了解Django的**MVC**是什么。  
相信大家都做好了项目的基本配置。  
开始吧
## 创建你的第一个应用   
什么是应用？
你现在打开手机，有微信、淘宝、支付宝、邮箱，他们都是手机上的应用，而手机系统就相当于项目。  
如果你现在打开**微信**，可以发现底下有四个区域，每一个区域也是一个小的应用，而微信就相当于项目。  
那么博客有几个应用呢？？  
我们先把一个博客应该有的内容先列出来：  
文章、标题、作者、创建时间、标签、分类、评论、阅读数、用户、图片、友情链接……一大堆东西。  
其实你想有什么，塞进去就好了。   
不过最好每次动手前，先想清楚那些功能是共通的和相似，整合到一块去，公共的也分出来。  
例如**阅读数**，这个功能放到哪里比较好呢？？  
这个功能最好单独拿出来，因为可以拓展成**总来访人数**、**今天来访人数**。  
讲那么多，动手吧。  
把终端切换到项目的根目录下（确保在虚拟环境中）  
`python manage.py startapp blog`  
上面这句代码的意思是创建一个名为blog的应用。  
`mv blog apps`把blog移动到apps目录下。  
移动到apps目录下是为了方便管理应用，全部堆到根目录下很难看。  
`touch apps/blog/urls.py`，在应用中创建一个名为urls.py的文件。  
## models.py  
这个文件主要是用来创建数据库键名和内容的索引的。  
结合这个应用的功能来说：
这个应用是我们博客的主体，博文方面的。  
我们一篇博文中的基本信息有：标题、作者、文章、创建时间、简介、图片还有一个索引。  
索引这个字段是关乎路由方面的知识，后面再讲。  
```python
from django.db import models
import markdown
# Create your models here.
# 生成一个基类，让其它类拥有该方法
# 这是用来把markdown格式的文本转化成html格式的方法
class BlogBase(models.Model):
    def body_markdown(self):
        mark = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
        ])
        self.body = mark.convert(self.body)
        self.toc = mark.toc
        return self.body
'''
讲解一下，下面的models.xxxx方法
models.CharField 这个字段是用来表示短语字段，必须带有最大长度的参数
models.TextField 这个字段是文本格式，也就是文章
models.DateTimeField 这个字段是用来获取时间的
models.SlugField 这个字段有点难翻译，由于Django是新闻方面公司放出来的一个开源项目
                属于新闻方面的术语。我们平时看新闻，控制新闻顺序的就是用slug了
                它是把新闻标题的文章转换为两到四个字或者单词来确定播放顺序的。
                香港澳门那边好像都是用这种。
                我们这里把它用作网址的后缀。
参数方面就不介绍了，看文档和复制粘贴翻译就好了
'''

class Blog(BlogBase):
    title = models.CharField(verbose_name="标题",max_length=50)
    body = models.TextField(verbose_name="内容")
    author = models.CharField(verbose_name="作者",max_length=50,default='sing')
    created_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True,verbose_name='修改时间')
    slug = models.SlugField(verbose_name="索引后缀",unique=True)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['-created_time']

    # 使对象在后台显示更友善
    def __str__(self):
        return "<Blog:%s>" % self.title

```  
## views.py  
这个文件的作用是视图逻辑。  
也就是我们打开[http://127.0.0.1:8000](http://127.0.0.1:8000)之类的效果。  
就是靠这个文件的方法呈现的，例如说打开上面的链接是看到首页，而看到文章详情页又是另外一种页面。  
就是靠这里的逻辑实现的。原理看代码的注释。  
```python
# 从Django的快捷方法中导入 渲染、要么获取对象要么404方法
from django.shortcuts import render,get_object_or_404
# 从当前目录下的models.py中导入Blog类
from .models import Blog

# 所有博客列表方法 首页的处理方法
def blog_list(request):
    context = {}   # 生成一个空字典
    context['blogs'] = Blog.objects.all() # 获取Blog中的所有对象

    # request 请求 意思是当我们在浏览器中访问 http://127.0.0.1:8000
    # 就相当于发送了一个请求给Django，当请求成功后
    # django就把context的内容在blog_list.html中渲染并返回给这个请求。
    # blog_list.html在后面环节再创建
    return render(request,'blog_list.html',context)

# 文章详情页内容的处理方法
def blog_detail(request,slug): # 接收请求和slug参数
    context = {}  # 生成一个空字典

    # 在Blog也就是我们的数据库中寻找有没有slug字段和传进来的slug字段匹配的
    # 没有，则返回404,有则返回该对象的内容
    context['blog'] = get_object_or_404(Blog, slug=slug)
    # blog_detail.html未创建
    return render(request,'blog_detail.html',context)
```
## admin.py
这是后台的字段参数，先复制吧，后面运行项目时，才能看到效果
```python
from django.contrib import admin
from .models import Blog
# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','slug', 'author', 'created_time', 'update_time')
```
## urls.py  
这是路由文件，现在项目中有两个urls.py文件。  
注意区分开来，一个是在mysite目录下，另一个在应用里面。  
讲之前先说明一下路由的作用是什么？  
路由的作用，用来配发地址的。
我们把网站比作是一个小区，小区中的门牌号就是网站的网址后缀。  
我们回去自己家，总有个门牌号吧，我们要通过门牌号来区分   
例如说我的域名是porksuimai.com这是小区  
而后面的django-1相当于门牌号。  
门牌号是唯一的，如果出现相同的门牌号，就会出现冲突。  
### 总路由  
我们项目的总路由在根目录下的mysite目录中的urls.py文件   
内容如下注意里面代码的注释：
```python
"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# 从django的核心方法导入管理员方法
from django.contrib import admin
# 从django的路由方法导入 路径、包括方法
from django.urls import path,include

urlpatterns = [
    # 根路径 从apps中的blog中导入urls.py文件，
    # 这里的意思就是包括了apps中的blog中urls.py的内容
    # 如果有多台路由器进行拼接经验的话，不难理解，这里相当与桥接路由器
    path('',include('apps.blog.urls')),
    # 下面的这个路径是后台管理路径，后面我们写博文都在这个网址写
    # http://127.0.0.1:8000/admin
    path('admin/', admin.site.urls),
]
```
### blog的路由  
看代码注释吧  
```python
# 从django的路由方法导入 路径、正则路径方法
from django.urls import path,re_path
# 从当前目录下导入views.py的内容
from . import views

urlpatterns = [
    # 下面方法中第一个参数是路径
    # 总路由也是为空，所以我们的博客列表就是首页
    # 当我们在浏览器打开 http://127.0.0.1:8000
    # 就会发送一个请求给django
    # django就会从路由器中寻找是否有这路径的，没有就会返回404
    # 有就寻找该路径对应的方法，也就是下面的第二个参数，  
    # 第三个参数，相当于是变量名，也就是说 blog_list = path('', views.blog_list)
    # 后面使用模板时会用到，现在知道一下就好了
    path('', views.blog_list,name='blog_list'),

    # re_path不难理解是正则匹配路径
    # 大家可以回头看一下views.py中的blog_detail函数
    # 它除了request参数还有一个slug参数
    # 解释一下这里的正则表达式吧：
    # 这是正则表达式匹配路径，/(?P<slug>[\w-]+)/
    # 以/开头 以/结束  括号()是括起来的的表达式作为一个分组
    # [\w-]是匹配任意字母数字和减号
    # (?P<slug>[\w-]+)就是把slug进行分组，匹配里面的[\w-]
    re_path('detail/(?P<slug>[\w-]+)/', views.blog_detail, name='detail'),
]
```  
