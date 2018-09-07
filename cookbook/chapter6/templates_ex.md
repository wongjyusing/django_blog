## 模板拓展  
注意，进行下面操作，务必把之前写好的模板文件保存一份到其它目录中，防止操作失误，导致前功尽废。  
还是那句话，为什么需要**模板拓展方法？**  
我现在写好了首页、博客列表页、文章详情页的内容。  
三个文件的内容如下：  
### 首页
```html
{% load diy_tags %}     {# 导入自定义标签 #}
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>首页</title>{# 这里有不同 #}
    <link rel="stylesheet" href="/static/css/base.css">
    {% block css_file %}{% endblock %}
    <link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">
    <script type="application/javascript" src="{% static 'js/jquery.min.js' %}"></script>
    <script type="application/javascript" src="{% static 'js/bootstrap.min.js' %}"></script>
</head>
<body>
    <header class="site-header">
        <div class="site-branding">
            <h1 class="site-title"><a href="{% url 'home' %}">花若盛開 蝴蝶自來</a></h1>
            <div class="site-introduction">这是我用Django2.0和bootstrap搭建的博客</div>
        </div>
        <nav class="navbar-default site-navigation" role="navigation">
            <div class="container-fluid" >
                <div class="navbar-header" >
                    <button type="button" class="navbar-toggle"  data-toggle="collapse" data-target="#navbar-collapse"><span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                    </button>
                </div>
            <div id="navbar-collapse" class="collapse navbar-collapse">
                <ul class="menu">
                    <li><a href="{% url 'home' %}">首页</a></li>{# 这里有不同 #}
                    <li><a href="{% url 'blog_list' %}">博客列表</a></li>{# 这里有不同 #}
                    <li><a href="#">文档</a></li>
                    <li><a href="#">关于</a></li>
                </ul>
            </div>
            </div>
         </nav>
    </header>

    <div class="site-me-widget-first">
        <h4 class="title">标签</h4>
        <hr>
        <div class="content community">
            {% get_blog_tag_list as tag_list %}  {# 把函数实例化为变量名 #}
            {% for tag in tag_list %}     {# 通过for循环遍历出内容 #}
                <li class="blog-type-tag"><a target="_blank" href="{% url 'blog_tag' tag.slug %}">{{ tag.name }}</a></li>
            {% empty %}   {# 这个empty是说，假如没有标签的话，显示下面p标签的内容 #}
                <p>暂无标签 敬请期待</p>
            {% endfor %}
        </div>
        <div class="content community">
            {% get_blog_type_list as type_list %}  {# 把函数实例化为变量名 #}
            {% for type in type_list %}     {# 通过for循环遍历出内容 #}
                <li class="blog-type-tag"><a target="_blank" href="{% url 'blog_type' type.slug %}">{{ type.name }}</a></li>
            {% empty %}   {# 这个empty是说，假如没有标签的话，显示下面p标签的内容 #}
                <p>暂无分类 敬请期待</p>
            {% endfor %}
        </div>
    </div>

    <footer>
        <div class="diy-card">
          <p>Copyright © 2018 Sing. Powered by Django.</p>
          <p>粤ICP备18079962号</p>
        </div>
    </footer>
</body>
</html>
```
### 博客列表页
```html
{% load diy_tags %}     {# 导入自定义标签 #}
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>博客列表</title>{# 这里有不同 #}
    <link rel="stylesheet" href="/static/css/base.css">
    <link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">
    <script type="application/javascript" src="{% static 'js/jquery.min.js' %}"></script>
    <script type="application/javascript" src="{% static 'js/bootstrap.min.js' %}"></script>
</head>
<body>
    <header class="site-header">
        <div class="site-branding">
            <h1 class="site-title"><a href="{% url 'home' %}">花若盛開 蝴蝶自來</a></h1>
            <div class="site-introduction">这是我用Django2.0和bootstrap搭建的博客</div>
        </div>
        <nav class="navbar-default site-navigation" role="navigation">
            <div class="container-fluid" >
                <div class="navbar-header" >
                    <button type="button" class="navbar-toggle"  data-toggle="collapse" data-target="#navbar-collapse"><span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                    </button>
                </div>
            <div id="navbar-collapse" class="collapse navbar-collapse">
                <ul class="menu">
                    <li><a href="{% url 'home' %}">首页</a></li>{# 这里有不同 #}
                    <li><a href="{% url 'blog_list' %}">博客列表</a></li>{# 这里有不同 #}
                    <li><a href="#">文档</a></li>
                    <li><a href="#">关于</a></li>
                </ul>
            </div>
            </div>
         </nav>
    </header>

    <div class="container"><!--容器-->
            <div class="row"><!--列-->
                <div class="col-xs-12 col-md-10"><!--文章列表-->
                    <div class="panel panel-default">
                        <div class="panel-heading">
                            <h3 class="panel-title" style="text-align: center;font-size: 40px">文章列表</h3>
                        </div>
                        <div class="panel-body">
                            {% for each in blogs %}
                                <div class="blog">
                                    <h3><a href="{% url 'detail' each.slug %}">{{ each.title }}</a></h3>

                                    <p class="blog-info">阅读数：({% read_count_tag each.slug %})&nbsp;&nbsp;分类：<a href="{% url 'blog_type' each.blog_type.slug %}">{{ each.blog_type }}</a>&nbsp;&nbsp;
                                        创建时间：{{ each.created_time|date:"Y-m-d" }}&nbsp;&nbsp;标签：{% for i in each.blog_tag.values %}
                                            <a href="{% url 'blog_tag' i.slug %}">{{ i.name }}</a>&nbsp;
                                            {% endfor %}
                                    </p>
                                    <p>{{ each.body_markdown|safe|truncatechars:120}}</p>
                                    <hr>
                                </div>
                            {% empty %}
                                <div class="blog">
                                    <h3>暂无博客，敬请期待</h3>
                                </div>
                            {% endfor %}
                        </div>
                    </div>
                </div><!--./col-md-10-->
                <div class="hidden-xs col-md-2"><!--文章分类-->
                    {# 分类 #}
                    <div class="panel panel-default">
                        <div class="panel-heading">全部分类</div>
                        <div class="panel-body blog-tags">
                          {% get_blog_type_list as type_list %}     {# 实例化函数名 #}
                          {% for type in type_list %}
                             <li class="blog-type-tag"><a href="{% url 'blog_type' type.slug %}">{{ type.name }}</a></li>
                          {% empty %}
                              <p>暂无分类 敬请期待</p>
                          {% endfor %}
                        </div>
                    </div>
                    {# 标签 #}
                    <div class="panel panel-default">
                        <div class="panel-heading">标签列表</div>
                        <div class="panel-body blog-tags">
                            {% get_blog_tag_list as tag_list %}
                            {% for tag in tag_list %}
                                <li class="blog-type-tag"><a href="{% url 'blog_tag' tag.slug %}">{{ tag.name }}</a></li>
                            {% empty %}
                                <p>暂无分类 敬请期待</p>
                            {% endfor %}
                        </div>
                    </div>
                </div><!--col-md-2-->
            </div><!--row-->
        </div><!--container-->

    <footer>
        <div class="diy-card">
          <p>Copyright © 2018 Sing. Powered by Django.</p>
          <p>粤ICP备18079962号</p>
        </div>
    </footer>
</body>
</html>
```
### 文章详情页
```html
{% load diy_tags %}     {# 导入自定义标签 #}
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>首页</title>{# 这里有不同 #}
    <link rel="stylesheet" href="/static/css/base.css">
    {% block css_file %}{% endblock %}
    <link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">
    <script type="application/javascript" src="{% static 'js/jquery.min.js' %}"></script>
    <script type="application/javascript" src="{% static 'js/bootstrap.min.js' %}"></script>
</head>
<body>
    <header class="site-header">
        <div class="site-branding">
            <h1 class="site-title"><a href="{% url 'home' %}">花若盛開 蝴蝶自來</a></h1>
            <div class="site-introduction">这是我用Django2.0和bootstrap搭建的博客</div>
        </div>
        <nav class="navbar-default site-navigation" role="navigation">
            <div class="container-fluid" >
                <div class="navbar-header" >
                    <button type="button" class="navbar-toggle"  data-toggle="collapse" data-target="#navbar-collapse"><span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                    </button>
                </div>
            <div id="navbar-collapse" class="collapse navbar-collapse">
                <ul class="menu">
                    <li><a href="{% url 'home' %}">首页</a></li>{# 这里有不同 #}
                    <li><a href="{% url 'blog_list' %}">博客列表</a></li>{# 这里有不同 #}
                    <li><a href="#">文档</a></li>
                    <li><a href="#">关于</a></li>
                </ul>
            </div>
            </div>
         </nav>
    </header>

    <div class="container">
        <div class="row">
            <div class="col-xs-12 col-sm-9">
                <div class="panel panel-default">
                    <div class="panel-heading">
                        <h3 class="panel-title" style="text-align: center;font-size: 40px">{{ blog.title }}</h3>
                    </div>
                    <div class="panel-body">
                      <p class="detail-nav"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;创建时间：{{ blog.created_time }}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;作者：{{ blog.author }}&nbsp;&nbsp;&nbsp;标签：{% for i in blog.blog_tag.values %}
                          <a href="{% url 'blog_tag' i.slug %}">{{ i.name }}</a>&nbsp;
                          {% endfor %}</p>

                        {{ blog.body_markdown|safe }}
                    </div>
                </div>
            </div>
            <div class="hidden-xs col-sm-3">
              <div class="diy-toc">
                  {{ blog.toc|safe }}
              </div>
            </div>
        </div>
    </div>

    <footer>
        <div class="diy-card">
          <p>Copyright © 2018 Sing. Powered by Django.</p>
          <p>粤ICP备18079962号</p>
        </div>
    </footer>
</body>
</html>
```  
有没有发现他们又臭又长啊？？而且发现哪里有问题的话，想修改也很麻烦啊。  
上面这份代码是用不了的，这是我以前写过的一个项目复制过来的，有些功能，不存在。不能直接使用。  
现在我想修改上面的代码，想找到错误的地方找不到。  
有没有更简洁的写法呢？？？
这个时候就要用到我们的**模板拓展方法**了。  
首先利用`{# 注释 #}`，把三个页面的不同的地方标注一下。大概是有5个到6个不同的地方。  
你自己的模板可能数量不一样。  
头部和底部的title标签不一样。  
我的头部导航部分的链接是有选中效果的，样式内容不一样。  
页面的主体内容不一样。  
那么就把一样的地方做成一个容器来接收不一样数据。  
## 基础的拓展语法
```html
{% extends 'base.html' %}   {# 拓展 装载内容的容器文件 #}

{% block title %}   {# block是块的意思 title是变量名  #}
    首页                  {# 首页 是我们需要传递的内容 空格不计算 #}
{% endblock %}      {# 结束拓展 #}

{% include 'base_right.html' %} {# 导入一个html的文件内容，后面会介绍 #}
```  
现在主要围绕着上面的第一条和第二段语句的使用进行讲解。  
前面说到需要一个容器。新建一个名为**base.html**的文件作为我们的容器。  
`touch templates/base.html`  
注意，进行以下的操作前请把之前做好的模板备份一份到其它目录中，以防不测（之前试过遇到停电）。  
## base.html
首先复制你认为代码量最多的一份文件的内容到**base.html**中。  
在**base.html**中，把之前用注释标注的地方，也就是三个文件不同之处，把他们的**内容**统统删掉。但是要保留**注释**。  
然后用`{% block title %}{% endblock %}`放到之前删掉的内容中。  
注意，上面的**tiele**是一个变量名，根据内容的含义来起变量名。我这里的例子是因为在模板文件的title标签的内容不同，所以给他命名为title。  
其它部位根据其内容含义，起一些见名知义的变量名。  
看例子  
```html
{# base.html #}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{% block title %}{% endblock %}</title>{# 这里有不同 #}
    <link rel="stylesheet" href="/static/css/base.css">
    {% block css_file %}{% endblock %} {# 需要导入的文件不同 #}
    <link rel="stylesheet" href="/static/css/bootstrap.min.css">
    <script type="application/javascript" src="/static/js/jquery.min.js"></script>
    <script type="application/javascript" src="/static/js/bootstrap.min.js"></script>
</head>
<body>
    <header class="site-header">
        <div class="site-branding">
            <h1 class="site-title"><a href="{% url 'home' %}">花若盛開 蝴蝶自來</a></h1>
            <div class="site-introduction">这是我用Django2.0和bootstrap搭建的博客</div>
        </div>
        <nav class="navbar-default site-navigation" role="navigation">
            <div class="container-fluid" >
                <div class="navbar-header" >
                    <button type="button" class="navbar-toggle"  data-toggle="collapse" data-target="#navbar-collapse"><span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                    </button>
                </div>
            <div id="navbar-collapse" class="collapse navbar-collapse">
                <ul class="menu">
                    <li {% block home_active %}{% endblock %}><a href="{% url 'home' %}">首页</a></li>{# 这里有不同 #}{# 选中效果 #}
                    <li {% block blog_active %}{% endblock %}><a href="{% url 'blog_list' %}">博客列表</a></li>{# 这里有不同 #}
                    <li><a href="#">行情分析</a></li>
                    <li><a href="#">关于</a></li>
                </ul>
            </div>
            </div>
         </nav>
    </header>
    {% block content %}{% endblock %}  {# 页面的大体内容不同 #}
</body>
</html>
```
当完成后，进行下一步
## blog_list.html
保留内容不相同的地方，也就是我们注释标注的地方。  
把其他相同的部分的内容全部去掉。  
并用在base.html定义的`{% block xxxx %}{% endblock %}`包裹住对应的内容。  
最后在文件的第一行写上`{% extends 'base.html' %} `  
最终效果如下：
```html
{% extends 'base.html' %}   {# 继承的模板文件 #}

{% block title %}   {# 这里是页面窗口的标题名 #}
    博客列表
{% endblock %}

{% block css_file %}       {# 这里是需要导入的css文件 #}
    <link rel="stylesheet" href="/static/css/blog.css">
{% endblock %}

{% block blog_active %} {# 这里是博客的点击效果 #}
    class="nav-active"
{% endblock %}

{% block content %}     {# 这里是内容 #}
    <div class="container"><!--容器-->
        <div class="row"><!--列-->
            <div class="col-xs-12 col-md-10"><!--文章列表-->
                <div class="panel panel-default">
                    <div class="panel-heading">
                        <h3 class="panel-title" style="text-align: center;font-size: 40px">文章列表</h3>
                    </div>
                    <div class="panel-body">
                        {% for each in blogs %}
                            <div class="blog">
                                <h3><a href="{% url 'detail' each.slug %}">{{ each.title }}</a></h3>
                                <p class="blog-info">
                                    <span class="glyphicon glyphicon-tag"></span><a href="{% url 'blog_type' each.blog_type.slug %}">{{ each.blog_type }}</a>&nbsp;&nbsp;
                                    <span class="glyphicon glyphicon-time"></span> {{ each.created_time|date:"Y-m-d" }}&nbsp;&nbsp;
                                </p>
                                <p>{{ each.body_markdown|safe|truncatechars:120}}</p>
                                <hr>
                            </div>
                        {% empty %}
                            <div class="blog">
                                <h3>暂无博客，敬请期待</h3>
                            </div>
                        {% endfor %}
                    </div>
                </div>
            </div><!--./col-md-10-->
            <div class="hidden-xs col-md-2"><!--文章分类-->
                <p>留空，占位</p>
            </div><!--col-md-2-->
        </div><!--row-->
    </div><!--container-->
{% endblock %}
```  
先完成blog_list.html文件。尝试运行项目看一下效果。  
和未修改前无误的话，继续改写home.html文件，blog_detail.html文件。  
由于本篇文章的代码量太多了，大家可以到[本链接](https://github.com/wongjyusing/wongyusing/tree/master/Python/python_web/django_learn/django_pock_suimai/day_234/pork_suimai/templates)中查看其他文件的优化效果。
下一章节讲解，总结Django写博客项目的技巧。
