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
'''
讲一下这里的设计思路
之前的写法功能单一。在我以前的项目中
个人空间只能在html文件，手写。如果写错，修改起来比较麻烦。
现在，我只需要在后台界面修改即可，不需要修改文件了。
现在这两个类，也就是数据库设计，可以拓展成个人空间、友情链接、书籍链接等各种链接
讲一下用法
以个人空间作为例子
首先在工具箱中的 分类名填写 个人空间
索引名填写 space
保存完成后

在ToolParameter
name填写GitHub
link填写你的github地址
tool_name选择 个人空间

img_link和introduction是可选参数。
例如github是用图片作为点击链接的，那就填写你的图片链接img_link。

如果你想要，当用户的鼠标移动到该链接上，会有提示文字或简介显示一个浮动窗口的话。
例如，鼠标移动到该链接上，浮现一段文字 ：“github 全球最大的Gay友交流网站”

'''

class ToolParameter(models.Model):
    name = models.CharField(max_length=64,verbose_name='链接名')
    link = models.URLField('友链地址', help_text='请填写http或https开头的完整形式地址')
    img_link = models.URLField('图片地址', help_text='请填写http或https开头的完整形式地址',null=True)
    introduction = models.TextField(verbose_name='简介',null=True)
    tool_name = models.ForeignKey(ToolName, verbose_name='工具分类', on_delete=models.CASCADE)
    class Meta:
        verbose_name = '工具'
        verbose_name_plural = '工具列表'
        ordering = ['id']  # 排序，按id排序

    # 使对象在后台显示更友善
    def __str__(self):
        return self.name
