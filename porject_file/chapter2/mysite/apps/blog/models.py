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
    def __str__(self):
        return self.name
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
    def __str__(self):
        return self.name


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
