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
