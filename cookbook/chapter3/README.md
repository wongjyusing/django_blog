## Django的模板语言   
最基础的三句：
```html
{{ xxxx.oooo }}   {# 变量语句 #}

{% for xxxx in xxxxs %}    {# 开头除了用for 还可以用if 等控制语句 #}
    {{ xxxx }}                  {# 这里是使用变量语句 #}  
{% endfor %}               {# 如果开头用了if 结尾要改成endif #}
                           {# 大多数控制语句都需要end和语句形式结尾 #}
                           {# 也有例外，例如url，还有些语句等到后面在进行讲解 #}

{# 我就不难猜了吧，我是注释 #}
```  
## html和Django基础配合写法  
下面展示的例子是最基础的知识，后续还有更高级的方法来减少我们的代码量。
### a标签
下面例子中**blog_list**是我们在urls.py中定义的方法的变量名  
`<a href="{% url 'blog_list' %}">博客列表</a>`  
传参：  
`<a href="{% url 'detail' each.slug %}">{{ each.title }}</a>`  
注意：控制语句是可以传参，由于文章详情页的处理方法是根据slug的值决定返回哪一篇博文，所以需要取里面的slug数据。
### H1  
例如说想要标题变得很醒目。  
`<h1>{{ blog.title }}</h1>`  
其他标签同理。  
### li标签  
```html
{% for blog in blogs %}
    <li><a href="{% url 'detail' blog.slug %}">{{ blog.title }}</a></li>
{% endfor %}
{# 通过这个方法就可以取出所有博文的链接 #}
```
## 关于前端页面的设计  
也就是我们的博客界面。希望大家都可以自己写出自己心中想要的博客界面。  
当然，也可以直接使用我提供的模板界面。  
不过我自己都嫌弃我现在的界面，因为实在是太刺眼了，文章主体这里颜色选得不好，太亮太刺眼了。  
我后续也会把这个界面用Vue.js重新设计，并把博客结构转化为书结构形式，有点类似于gitbook吧。  
## 关于前端学习的心得
提供的模板是我花了一天左右才写出来了。  
我当时没有任何前端知识，还是硬生生被我写出来了。
技巧在于：
首先，你需要一只笔和一张纸。  
把你想要的博客界面画出来，例如首页要怎么样的，详情页是怎么样的。画出来。  
然后，把这个页面分为三部分，头、躯干、脚。  
每个部位再细分一下。
不懂的地方，谷歌一下，写一个。
一个一个的写出来。
CSS也是一样，`a标签不要下划线、li标签不要点……`  
最后，把写好的代码像乐高积木拼接起来就好了。  
你们可以打开我提供的模板，页面也就三个部分就搞定了。  
写完以后，你就有了前端的基础知识了。  
先不要使用其他例如Vue的框架。他们的语法使用会和python的web框架起冲突。Tornado、Flask我都试过，会出现错误的。  
关于vue的解决方案有的，如果你会vue.js，也请先了解一下后端方面的知识。  
后期的话，我也会讲Django和Vue配合搭建博客的教程。   
初学者可以先利用**Bootstrap**来辅助布局方面的工作，响应式可以在以后学了前端后再添加。  
大家可以先练习怎么用模板语言配置好模板的页面后，再进行后面的内容。
## CSS和JS导入
如下：
```html
<link rel="stylesheet" href="/static/css/base.css">
<link rel="stylesheet" href="/static/css/blog.css">
<link rel="stylesheet" href="/static/css/bootstrap.min.css">
<script type="application/javascript" src="/static/js/jquery.min.js"></script>
<script type="application/javascript" src="/static/js/bootstrap.min.js"></script>
```
如果部署上线的话需要修改为下面的这种形式，这也是模板控制语句的。
```html
<link rel="stylesheet" href="{% static 'css/blog.css' %}">
<script type="application/javascript" src="{% static 'js/jquery.min.js' %}"></script>
```
