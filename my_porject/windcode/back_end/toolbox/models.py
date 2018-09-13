from django.db import models

# Create your models here.
class ToolName(models.Model):
    name = models.CharField(max_length=64,verbose_name='分类名')
    slug = models.SlugField(unique=True,verbose_name='索引名')

    class Meta:
        verbose_name = '工具箱'
        verbose_name_plural = '工具箱列表'
        ordering = ['id']  # 排序，按id排序

    # 使对象在后台显示更友善
    def __str__(self):
        return self.name


class ToolParameter(models.Model):
    name = models.CharField(max_length=64,verbose_name='链接名')
    link = models.URLField('友链地址', help_text='请填写http或https开头的完整形式地址')
    img_link = models.URLField('图片地址', help_text='请填写http或https开头的完整形式地址',blank=True)
    introduction = models.TextField(verbose_name='简介',blank=True)
    tool_name = models.ForeignKey(ToolName, verbose_name='工具分类', on_delete=models.CASCADE)
    class Meta:
        verbose_name = '工具'
        verbose_name_plural = '工具列表'
        ordering = ['id']  # 排序，按id排序

    # 使对象在后台显示更友善
    def __str__(self):
        return self.name

class MySite(models.Model):
    name = models.CharField(max_length=64,verbose_name='网站名')
    introduction = models.CharField(max_length=100,verbose_name='简介')
    powered = models.CharField(max_length=100,verbose_name='设计者信息',help_text='Copyright © 2018 Sing. Powered by Django.')
    approval_number = models.CharField(max_length=100,verbose_name='审批号')

    class Meta:
        verbose_name = '网站信息'
        verbose_name_plural = '网站信息列表'
        ordering = ['id']  # 排序，按id排序

    # 使对象在后台显示更友善
    def __str__(self):
        return self.name
