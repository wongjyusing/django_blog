## 声明
暂时做半分离，没有用到node.js来作为服务器。  
因为vue的脚手架还不是很会（刚学完vue的基础知识）  
只能做到半分离。  
这个是用来练习vue的语法项目过程。为后续的**真·前后端分离**铺路   
同时后面的评论系统的前端也会用到这里的知识。   
本次只做我之前一直想要的GitBook的效果。主要是为了做像现在的一系列教程的容器，和普通的博客文章进行区别。  
下一次，直接使用vue-cil。（可能会自己写评论编辑器，找不到免费好看的）  
大家可以去vue的论坛看一下他们的编辑器，真的好漂亮，好骚。      
## Django前后端分离设计  
前后端分离，这个名词就不使用文皱皱的解释了。  
需要文皱皱解释的自行谷歌一下`前后端分离`  
结合这个项目来解释**前后端分离**。  
之前我们使用Django模板语言来在前端呈现内容。  
现在我们用Vue.js来呈现。  
简单来说，之前我们靠views.py返回html文件来渲染内容。  
现在views.py只返回json数据，模板上用Vue渲染数据。  
最直接说法，**不使用Django的模板语言**。  
话不多说，事不宜迟。开始。  
## 创建项目
创建一个全新的项目。下面的**windcode**是我一直想要的域名。可惜拿不到。
只好取个[porksuimai.com](porksuimai.com), 中文的意思是广东早茶的点心**蟹黄干蒸**（叉烧包、糯米鸡、蛋挞、凤爪、肠粉、牛百叶，都被人注册了，唉）。  
`django-admin startproject windcode`   
`cd windcode`  
`mkdir front_end back_end`  
配置过程参考前面的django项目基础配置。  
## 创建前后端应用  
`python manage.py startapp books`  
`python manage.py startapp index`  
`touch books/urls.py`  
`touch index/urls.py`  
`mkdir index/templates`  
`mv index front_end`  
`mv books back_end`  
完成后，目录结构如下：
```tree
├── back_end                          # 后端应用目录
│   └── books                         # 书结构应用目录
│       ├── admin.py
│       ├── apps.py
│       ├── __init__.py
│       ├── migrations
│       │   └── __init__.py
│       ├── models.py
│       ├── tests.py
│       ├── urls.py
│       └── views.py
├── front_end                         # 前端应用目录，
│   └── index                         # 负责所有应用前端处理
│       ├── admin.py
│       ├── apps.py
│       ├── __init__.py
│       ├── migrations
│       │   └── __init__.py
│       ├── models.py
│       ├── templates
│       ├── tests.py
│       ├── urls.py
│       └── views.py
├── manage.py                         # 调度文件,主要文件
└── windcode                          # 项目配置和路由
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-36.pyc
    │   └── settings.cpython-36.pyc
    ├── settings.py                   # 主要配置文件
    ├── urls.py                       # 总路由
    └── wsgi.py

```
