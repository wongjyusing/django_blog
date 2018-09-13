from django.db import models

# Create your models here.
# 生成基类，减少代码量
class BookBase(models.Model):
    # 本来有把内容转化成markdown的函数。
    # 经测试，json格式的输出，无法输出该函数内容，
    # 考虑后决定在前端转化markdown格式
    # 使对象在后台显示更友善
    def __str__(self):
        return self.name

class Book(BookBase):
    name = models.CharField(max_length=64,verbose_name='书名')
    slug = models.SlugField(unique=True,verbose_name='索引后缀')
    introduction = models.TextField(verbose_name='书的简介')
    status_models = models.CharField(max_length=64,verbose_name='状态',default='未完成，敬请期待')
    author = models.CharField(verbose_name='作者',default='Sing',max_length=50)
    created_time = models.DateTimeField(verbose_name='创建时间',auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='修改时间',auto_now=True)
    class Meta:
        verbose_name = '书本'
        verbose_name_plural = '图书馆'
        ordering = ['id']       # 排序，按id排序

class Chapter(BookBase):
    name = models.CharField(max_length=64,verbose_name='章节名')
    slug = models.SlugField(unique=True,verbose_name='索引后缀')
    body = models.TextField(verbose_name='章节内容')
    page_num = models.IntegerField(verbose_name='顺序',help_text='替换Django自带的id值，用于控制章节顺序')
    book_name = models.ForeignKey(Book, verbose_name='所属书名', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '章节'
        verbose_name_plural = '章节列表'
        ordering = ['page_num']       # 排序，按id排序

class Section(BookBase):
    name = models.CharField(max_length=64,verbose_name='小节名')
    slug = models.SlugField(unique=True,verbose_name='索引后缀')
    body = models.TextField(verbose_name='章节内容')
    page_num = models.IntegerField(verbose_name='顺序',help_text='替换Django自带的id值，用于控制章节小节顺序')
    chaptet = models.ForeignKey(Chapter, verbose_name='所属章节', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '章节小节'
        verbose_name_plural = '章节小节列表'
        ordering = ['page_num']       # 排序，按id排序
