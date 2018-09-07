## 博客的标签和类型
本章节开始后，先不要动手，先过一边大概内容后，再决定你的博客要设计那一种类型。  
而且会介绍Django的**自定义模板标签**、**模板拓展方法**、可以很大程度上减少你的代码量。  
一开始，会讲解博客的标签，分类的数据库设计方面。再讲如何使用模板拓展方法，减少代码。  
讲解完，自定义模板标签后，会让你的博客项目像乐高积木一样，就可以拼凑起来。  
## 开始  
回头阅读如何创建和配置Django项目，创建一个新的mysite项目。和新建一个名为blog的应用。  
由于之前的项目是生成了数据库，删除它比较麻烦，可以删但现在是文字讲解，讲解起来比较麻烦。  
当练习一下吧。如果你要偷懒的话也可以到我的github中下载一个[Django的基础配置文件](https://github.com/wongjyusing/django_blog/tree/master/django_base)  
下载名为mysite的目录即可。  
下载完后自行创建templates、static、apps目录。  
并依次执行下面的命令
```python
python manage.py startapp blog

mv blog apps

touch apps/blog/urls.py
```
## models.py  
打开我们在apps/blog/models.py文件，写入以下内容：
这个版本是博客标签和分类同时存在的版本。  
如果你是只要分类不要标签的话，把关于标签的内容去掉即可，只要标签的同理。  
```python
from django.db import models
import markdown
# Create your models here.
# 生成基类，减少代码量
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

# 标签
class BlogTag(BlogBase):
    name = models.CharField(max_length=64,verbose_name='标签名')
    slug = models.SlugField(unique=True，verbose_name='标签后缀')
    body = models.TextField(verbose_name='标签简介')
    class Meta:
        verbose_name = '标签'
        verbose_name_plural = '标签列表'
        ordering = ['id']       # 排序，按id排序
    # 使对象在后台显示更友善

# 标签
class BlogType(BlogBase):
    name = models.CharField(max_length=64,verbose_name='类型名')
    slug = models.SlugField(unique=True，verbose_name='类型后缀')
    body = models.TextField(verbose_name='类型简介')
    class Meta:
        verbose_name = '标签'
        verbose_name_plural = '标签列表'
        ordering = ['id']       # 排序，按id排序
    # 使对象在后台显示更友善



class Blog(BlogBase):
    title = models.CharField(verbose_name='标题',max_length=50)
    body = models.TextField(verbose_name='文章')
    author = models.CharField(verbose_name='作者',default='sing',max_length=50)
    created_time = models.DateTimeField(verbose_name='创建时间',auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='修改时间',auto_now=True)
    slug = models.SlugField(verbose_name='后缀',unique=True)

    blog_type = models.ForeignKey(BlogType, verbose_name='博客类型', on_delete=models.CASCADE)

    blog_tag = models.ManyToManyField(BlogTag,verbose_name='博客标签')

    '''
    有没有发现上面的BlogType和BlogTag只是名字不一样
    他们的内容都是一样的，不同的地方在于他们在BLog这个类中的关系
    blog_type是外键关联，
    blog_tag是多对多关系

    区别在于一篇博文只有一个 类型，
    但可以有多个 标签  
    现在的项目是两种类型同时存在，
    注意，使用多对多关系也就是标签的话，
    返回的内容是一个列表，需要用到for循环方可取出里面的内容

    blog_type里面的on_delete=models.CASCADE参数的意思是
    如果删除了该分类，该分类的内容也就是博文也会被删除掉。

    '''

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['-created_time']

    # 使对象在后台显示更友善
    def __str__(self):
        return "<Blog:%s>" % self.title

    # 分页
    def get_pre(self):# 上一页
        return Blog.objects.filter(id__lt=self.id).order_by('-id').first()

    def get_next(self):#下一页
        return Blog.objects.filter(id__gt=self.id).order_by('id').first()

```
先不要敲代码，想一下，你的博客还需要什么内容，需要展示什么内容？？  
阅读数、图片和文章列表分页这部分后面会讲到，可以先不考虑。  
其实上面的代码都是根据前端方面去设计的，可以说成是**前端决定后端**  
拿起你的纸和笔，画一下你的博客的首页、博客列表页、文章详情页。  
按**标签**归档页和按**分类**归档页，其实和**博客列表页**可以说基本上一模一样，就名字不一样。  
可以先不画，后面暂时也不用写，等介绍到模板拓展方法再写。  
## views.py
视图部分就相对于之前多了一个分页的通用函数，其它函数都很简单的啦。  
```python
from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Blog,BlogTag,BlogType
# Create your views here.

# 分页通用函数，第一个参数是内容列表，第二个参数是页码
def page_gen(contact_list,page):
    # 分页规则 ，第一个参数，内容列表，第二个参数，每页多少内容。第三个参数，孤儿参数
    # 孤儿参数： 假如现在总共有12篇博文，正常来说每页有10篇博文，那么总页码应该有两页。
    # 但采取了孤儿参数后，第一页会有12篇博文，没有了第二页。
    # 除非有13篇博文，才会出现第二页
    paginator = Paginator(contact_list, 10,2)
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # 如果传入的参数不是整数类型，返回第一页内容
        # 假如用户输入page=abcd或者其他字符，返回第一页内容
        contacts = paginator.page(1)
    except EmptyPage:
        # 如果传入的页码大于最大的页码数，返回最后一页的内容
        # 现在总共有5页，如果用户输入第6页则返回第5页的内容
        contacts = paginator.page(paginator.num_pages)

    return contacts

# 首页
def home(request):
    return render(request,'home.html')



# 所有博客列表
def blog_list(request):
    context = {}

    contact_list = Blog.objects.all()
    # 从请求中查找是否有page参数，如果有则取page的参数
    # 没有则取1
    page = request.GET.get('page',1)

    context['blogs'] = page_gen(contact_list,page)

    return render(request, 'blog_list.html', context)


# 按标签分类的博客列表
def blog_tag(request, slug):
    context = {}
    # 在BlogTag中也就是我们的数据库中寻找有没有slug字段和传进来的slug字段匹配的
    blog_tag = get_object_or_404(BlogTag, slug=slug)

    # 从Blog中寻找是在该标签下的文章列表
    contact_list = Blog.objects.filter(blog_tag=blog_tag)

    page = request.GET.get('page', 1)
    # 从请求中查找是否有page参数，如果有则取page的参数
    # 没有则取1
    context['blogs'] = page_gen(contact_list, page)


    return render(request, 'blog_tag.html', context)
# 按类型分类页
def blog_type(request, slug):
    context = {}
    # 在BlogTag中也就是我们的数据库中寻找有没有slug字段和传进来的slug字段匹配的
    blog_type = get_object_or_404(BlogType, slug=slug)

    # 从Blog中寻找是在该标签下的文章列表
    contact_list = Blog.objects.filter(blog_type=blog_type)

    page = request.GET.get('page', 1)
    # 从请求中查找是否有page参数，如果有则取page的参数
    # 没有则取1
    context['blogs'] = page_gen(contact_list, page)

    return render(request, 'blog_type.html', context)


def blog_detail(request,slug): # 接收请求和slug参数
    context = {}  # 生成一个空字典

    # 在Blog也就是我们的数据库中寻找有没有slug字段和传进来的slug字段匹配的
    # 没有，则返回404,有则返回该对象的内容
    context['blog'] = get_object_or_404(Blog, slug=slug)
    # blog_detail.html未创建
    return render(request,'blog_detail.html',context)
```
上面的代码基本上，没几个地方值得优化了。  
关于页码的使用留到模板方面再讲。  
## urls.py
相信大家看下面的内容都没什么问题，有问题回头看**最最基础的博客**
```python
from django.urls import path,re_path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('blog_list/', views.blog_list, name='blog_list'),
    re_path('type/(?P<slug>[\w-]+)/', views.blog_tag, name='blog_type'),
    re_path('tag/(?P<slug>[\w-]+)/', views.blog_tag, name='blog_tag'),
    re_path('detail/(?P<slug>[\w-]+)/', views.blog_detail, name='detail'),

]

```
## admin.py
后台管理，这里给个装*的机会大家，留意最后的注释，运行项目并进入后台，有个小彩蛋哦。  
```python
from django.contrib import admin
from .models import Blog, BlogTag,BlogType
# Register your models here.

@admin.register(BlogType)
class BlogTypegAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'slug',)

@admin.register(BlogTag)
class BlogTagAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'slug',)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'author', 'created_time', 'update_time')

admin.site.site_header = '恭喜发财'
admin.site.site_title = '最帅的管理员'
```  
我们的项目的后端就基本上完成了，但请大家先不要敲代码。  
接下来的内容可以让你的项目开发过程少了很多坑。  
下一篇提前讲**Django的自定义模板标签**   
通常这个内容都是放到后面，这里提前讲是为了拓展大家的开发思路。  
因为就我个人来讲，开发思路比写代码重要。  
思路理清了。做什么都比别人好。
