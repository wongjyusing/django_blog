## 分支测试总结  
经过测试，之前的项目结构方面设计失误，存在好多问题。  
- 接口传输的内容过于单一（功能单一）  
- 前端Vue.js要打开几个接口来获取数据  
- 未能使用到Vue.js的脚手架  
- 路由分发机制不完善  
- Vue.js脚手架中有路由器，后期要想办法使用到。  

## 假·前后端分离的后续规划  
### 项目结构  
依次执行下面的命令  
```linux
django-admin startproject windcode

cd windcode

mkdir static front_end back_end

mkdir static/css               

mkdir static/js

python manage.py startapp blog

python manage.py startapp book

python manage.py startapp toolbox

python manage.py startapp index  

python manage.py startapp comment

mv blog back_end

mv book back_end

mv toolbox back_end

mv comment back_end

mv index front_end

touch back_end/api_url.py

touch back_end/api_views.py

touch back_end/__init__.py

touch front_end/index/urls.py

```
得到的项目结构如下（留意注释）：  
```tree
.
├── back_end                            # 后端应用目录
│   ├── api_url.py                      # api路由文件
│   ├── api_views.py                    # api数据处理文件
│   ├── blog                            # 博客应用
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── __init__.py
│   │   ├── migrations
│   │   │   └── __init__.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   └── views.py
│   ├── book                            # 书结构应用
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── __init__.py
│   │   ├── migrations
│   │   │   └── __init__.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   └── views.py
│   ├── comment                          # 评论应用
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── __init__.py
│   │   ├── migrations
│   │   │   └── __init__.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   └── views.py
│   ├── __init__.py                      # 声明back_end是python的一个包
│   └── toolbox                          # 通用工具应用
│       ├── admin.py
│       ├── apps.py
│       ├── __init__.py
│       ├── migrations
│       │   └── __init__.py
│       ├── models.py
│       ├── tests.py
│       └── views.py
├── front_end                           # 前端应用
│   └── index
│       ├── admin.py
│       ├── apps.py
│       ├── __init__.py
│       ├── migrations
│       │   └── __init__.py
│       ├── models.py
│       ├── tests.py
│       ├── urls.py                     # 前端路由配置
│       └── views.py
├── manage.py                           # 主要控制文件
├── static                              # 静态文件目录
│   ├── css
│   └── js
└── windcode                            # 项目配置目录
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-36.pyc
    │   └── settings.cpython-36.pyc
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```
上面这种设计，目的是不使用后端应用中的views.py。  
处理方法全部集中到**api_views.py**集中处理。由**api_url.py**进行配发。  
其实可以把后端的内容设为一个应用，全部数据写到一个models.py中，但这样写，不美观。  
像现在的分开写，我们只需要编写应用中的models.py和admin.py即可。  
然后在**api_views.py**中。根据页面的需求输出内容。  
现在主要的输出有以下几个页面：
- 首页
- 博客列表页
- 博客详情页
- 书结构页（单独存在，区别于其它页面，界面结构完全不同）  
- 关于页  

这次，把博客标题也要后台的输出来，举个例子吧。  
现在不知道你们看到的标题是**花若盛開 蝴蝶自來**还是**阿星的博客**。  
这个部分也弄成后台输出吧。尽量把这个博客做到**开箱即用**的效果。  
而又不需要去修改代码。尽量都在后台处理。  
这个部分放到**通用工具**的modesl.py中。  
## 关于api_views.py的编写示例  
```python
from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
from django.core import serializers
import json

from .blog import models as BlogModel
from .book import models as BookModel
from .toolbox import models as ToolBox

# 博客列表页
def blog_list(request):
    context = {}
    try:
        # 获取博客的所有对象
        blog = BlogModel.Blog.objects.all()
        # 通用信息获取，包括博客的标题、个人中心、友情链接、书本链接、等通用信息
        toolbox = ToolBox.ToolParameter.objects.all()
        # 让前端知道数据获取成功
        context['msg'] = 'success'
        # 让前端知道匹配那种处理方法
        context['data_type'] = 'blog_list'
        # 对获取的数据进行格式化处理
        context['toolbox'] = json.loads(serializers.serialize("json", toolbox))
        context['blogs'] = json.loads(serializers.serialize("json", blog))
    except Exception as e:
        context['msg'] = 'ERROR'

    return JsonResponse(context,json_dumps_params={'ensure_ascii':False})
```  
上面还有个地方没写到的是，关于博客内容的转换成html。  
之前写过的一个函数，忘记放在哪里了。专门处理markdown转html并生成锚点的。  
正式改造时再添加进去。  
