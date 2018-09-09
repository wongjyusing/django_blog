## 通用工具  
 阅读以下的内容前，必须会用自定义模板标签，不然你看不懂，自然也学不会。  
 请回到前面的内容学习自定义模板标签。
****
这次重构代码，又让我发现了可以优化的地方。  
这次的发现是从**博客主体的分类**，这个关键点发现的。  
先看一下以前的写法。  
首先，创建一个新的应用。  
`python manage.py startapp book_friend`
打开models.py写入以下内容。  
```python
from django.db import models

# Create your models here.
class FriendLink(models.Model):
    name = models.CharField(max_length=64)
    link = models.URLField('友链地址', help_text='请填写http或https开头的完整形式地址')

    class Meta:
        verbose_name = '友情链接'
        verbose_name_plural = '友情链接列表'
        ordering = ['id']  # 排序，按id排序

    # 使对象在后台显示更友善
    def __str__(self):
        return self.name


class BookLink(models.Model):
    name = models.CharField(max_length=64)
    link = models.URLField('友链地址', help_text='请填写http或https开头的完整形式地址')

    class Meta:
        verbose_name = '书籍'
        verbose_name_plural = '书籍链接列表'
        ordering = ['id']  # 排序，按id排序

    # 使对象在后台显示更友善
    def __str__(self):
        return self.name
```
有没有发现他们的代码只是个类名不一样啊？？  
使用方法，写两个自定义模板标签函数。  
如下：
```python
# pork_suimai/apps/blog/templaatetags/diy_tags
from django import template     # 从Django中导入模板方法
from ..models import FriendLink,BookLink
from django.db.models.aggregates import Count   # 从django的数据库模型总数中导入计数方法
register = template.Library()   # 注册   模板的库   Library 图书馆，可以理解为放书进去，



@register.simple_tag
def get_friend_link(): # 获取友情链接列表
    return FriendLink.objects.all()



@register.simple_tag
def get_book_link(): # 获取友情链接列表
    return BookLink.objects.all()
```  
以上的写法只是1+1=2。  
现在让我们来1+1=N  
## 新的写法  
新建一个应用：  
`python manage.py startapp toolbox`   
创建自定义模板标签diy_tools.py,  
依次在项目根目录下执行下面的代码。  
```python
mkdir toolbox/templatetags

touch toolbox/templatetags/__init__.py

touch toolbox/templatetags/diy_tools.py

mv toolbox apps
```  
打开toolbox中的models.py文件。  
写入以下的内容  
#### models.py
```python
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

其他像友情链接之类的也同理
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
```  
#### diy_tools.py
```python
from django import template     # 从Django中导入模板方法
from ..models import ToolName
from django.db.models.aggregates import Count   # 从django的数据库模型总数中导入计数方法
register = template.Library()   # 注册   模板的库   Library 图书馆，可以理解为放书进去，


'''
下面的这个函数，我就不写了，你们自己写。
给个提示，和在blog应用中views.py中的blog_type函数很像。
不过，不可以使用get_objects_404这个方法，会报错。
要用try这个方法获取对象，具体函数翻阅文档。
在文档的基础部分有写。
还有try不成功的话需要返回一个空列表还是None，大家想一下这个问题。

还有一点，这个应用不用编写urls.py、views.py
但要写admin.py文件，写法对照前面的写就好了。
彩蛋部分不用写到toolbox中的admin.py中。
一个项目写一次就好了。

'''

@register.simple_tag
def get_tools(slug):
    pass
```  
前端模板语句还有一两个坑。  
需要大家自己查阅文档来解决。  
****
上面的内容可以自行解决的话，后面的阅读计数功能都可以自行写出，
- 关于Django发送cookie的内容。   
- 关于models的IntField的知识   

利用上面的这些这两个知识点即可实现阅读计数功能。  
后续的内容除了评论，都只提供思路，代码方面就不给了。  
前面的博客主体为大家填了太多坑，剩下的坑都比较浅，都是可以跳出来的。又不是那种掉进去爬不上来的坑。
