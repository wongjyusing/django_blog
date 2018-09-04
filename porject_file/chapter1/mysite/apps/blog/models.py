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
    title = models.CharField(verbose_name="标题")
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
