## 运行项目前的必要操作  
我们的应用写好了，我们需要在项目中应用我们的**应用**。  
打开settings.py，找到INSTALLED_APPS进行添加  
```python
# Application definition
# 定义应用的地方
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'apps.blog', # 加上左边的这句内容，养成良好习惯在后面加上逗号
]
```  
在templates目录下生成我们的模板文件blog_list.html和blog_detail.html文件  
先不要复制之前的体验项目的文件，接下来要讲模板语法。  
### blog_list.html
```html
<!DOCTYPE html>
<html lang="en" dir="ltr">
    <head>
        <meta charset="utf-8">
        <title>测试</title>
    </head>
    <body>
        {% for blog in blogs %}
            {{ blog.title }}
        {% endfor %}
    </body>
</html>
```
### blog_detail.html
```html
<!DOCTYPE html>
<html lang="en" dir="ltr">
    <head>
        <meta charset="utf-8">
        <title>{{ blog.title }}</title>
    </head>
    <body>
        {{ blog.body_markdown|safe }}
    </body>
</html>
```   
### 新建应用或修改models.py后的必要操作
所有操作都在根目录下，请保证你在**虚拟环境**中
生成数据库迁移文件  
`python manage.py makemigrations`  
生成数据库  
`python manage.py migrate`  
创建超级管理员（这个只需要一次就好了，不用每次都创建）  
`python manage.py createsuperuser`  
根据提示依次输入信息即可。
## 运行项目   
`python manage.py runserver`  
浏览器打开`http://127.0.0.1:8000/`即可看到效果。  
一个空白页对吧？？？空白页说明运行成功。  
空白的原因是因为我们的数据库还没有内容，  
打开[http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)  
会有一个登录界面，输入你刚才设置的帐号密码（忘记了，重新设定一个）。  
登录完成后会看到一个后台管理页面。  
点击**文章**后面的**增加**写你的第一篇博文吧。  
没有markdown类型的文章可以复制下面的内容哦。  
注意，索引的内容必须为英文、数字和-号，其他字符不可以设置，建议刚开始就先设置成`111`吧。方便我继续讲解。
```markdown
### 新建应用或修改models.py后的必要操作
所有操作都在根目录下，请保证你在**虚拟环境**中
生成数据库迁移文件  
`python manage.py makemigrations`  
生成数据库  
`python manage.py migrate`  
创建超级管理员（这个只需要一次就好了，不用每次都创建）  
`python manage.py createsuperuser`  
根据提示依次输入信息即可。
## 运行项目   
`python manage.py runserver`  
浏览器打开`http://127.0.0.1:8000/`即可看到效果。  
一个空白页对吧？？？空白页说明运行成功。  
空白的原因是因为我们的数据库还没有内容，  
打开[http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)  
会有一个登录界面，输入你刚才设置的帐号密码（忘记了，重新设定一个）。  
登录完成后会看到一个后台管理页面。  
点击**文章**后面的**增加**写你的第一篇博文吧。  
没有markdown类型的文章可以复制下面的内容哦。  
```
保存后，回到[http://127.0.0.1:8000/](http://127.0.0.1:8000/)看一下效果。  
出现了刚才设定的文章标题。  
再打开[http://127.0.0.1:8000/detail/111/](http://127.0.0.1:8000/detail/111/)可以看到刚才写的文章内容。  
为什么会出现标题、文章的内容呢？  
这个涉及到Django的**模板语言**，下一章节专门讲模板语言和我学习前端的方法。  
大家可以尝试在blog_detail.html加入以下的内容试试看。  
```html
<a href="{% url 'blog_list'%}">博客列表</a>
{{ blog.body }}
{{ blog.title }}
{{ blog.author }}
{{ blog.created_time }}
{# 先不要在blog_list.html中尝试，因为涉及到列表的关系，很容易报错的哦 #}
```  
接下来，讲一下前端也就是浏览器中的内容是怎么来的？。  
## 回顾  
不知道大家有没有发现，我们的根目录下多了一个叫**db.sqlite3**的文件。  
这个就是我们的数据库。用编辑器打开它试试，可以看到一大堆乱码和一丢丢我们可以阅读的信息。  
不要修改里面的内容哦，我们只是看看。  
它是用来存放我们的数据的，我们在[http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)添加的内容都会存放到db.sqlite3。  
那么它是怎么产生的呢？  
首先sqlite3是属于关系型数据库，而它的键名都是在我们的models.py中定义的。
我们在后台写入内容后，内容存储到了数据库后。  
结合这个博客来说，我们在浏览器打开`http://127.0.0.1:8000/`，就发送了一个请求给Django。  
Django就会从总路由中（urls.py）寻找匹配`http://127.0.0.1:8000/`的方法。  
注意：总路由（mysite/urls.py）是包括/包含了blog中的urls.py的内容的。  
然后该路径匹配的处理方法是在views.py中的**blog_list**函数。  
该函数返回的结果在**blog_list.html**上渲染**Blog的全部对象**。  
Blog可以看成是关系型数据库的一个表，或者说是非关系型数据库的一个集合。  
所以blog_list函数返回的是一个列表内容，
在blog_list.html中，我们需要一个for循环来把里面的内容遍历出来方可使用。  
其实上面的内容涉及到设计模式的**MVC**  
### MVC
models.py，就是M，也就是数据模型  
views.py，视图，也可以说是视图逻辑  
模板语言，是我们在html文件中写的大括号，就是C。控制命令。  
我这里就不复制网上的说法，给个链接让大家看看[MVC](https://baike.baidu.com/item/MVC%E6%A1%86%E6%9E%B6/9241230?fr=aladdin&fromid=85990&fromtitle=MVC)，我的习惯是结合项目来讲解。  
如果还不明白数据是如何来到网页上的话，可以看一下以下的顺序，并结合项目中的代码观察一下。  
```python
# python manage.py runserver  运行项目
# 浏览器中输入http://127.0.0.1:8000 打开首页
# django接受到请求，匹配地址，成功
# 寻找该地址的处理方法，views.py中blog_list函数
# 该方法是生成一个空字典，
# 把数据库中名为Blog的表单的所有对象，
# 以键值对的形式赋值给blogs这个键名，
# 并以blog_list.html作为容器，渲染blogs的内容到相应中
# 通过模板中的控制语句，控制我们想要呈现的内容
# 最后我们就可以在浏览器中看到该页面了
```  
### 后台  
之前说过admin.py文件的内容，运行起来才能看到效果。  
大家先打开`http://127.0.0.1:8000/admin/`  
点击**文章**，可以看到一个表单。  
再打开admin.py，有没有发现，有些地方很相似啊？？  
让我们把admin.py中的**id**和**title**的位置替换一下并保存吧。  
在回头看一下后台页面？？  
相信这个顺序比较符合我们的查看习惯。  
