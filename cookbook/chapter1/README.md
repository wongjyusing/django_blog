## 什么是Django？  
Python的一个web框架。  
好了说完了。  
与其说Django是什么，不如说成是**Django可以做什么？**  
Django可以开发API接口、网站的管理后台、也可以展示前端页面。  
其实讲那么多也都是废话。  
动手才是最实际的。  
不过动手前，可以先了解一下到底什么是博客。  
如果你有python3基础的话，可以把这个[最基础的博客](https://github.com/wongjyusing/django_blog/tree/master/porject_file/chapter1)。git下来先尝试一下。  
再决定是否继续阅读后面的内容。
启动方法和安装方法都放到了项目的README.md里面。  
没有python3基础的话，先去学习变量、函数、字典、包的引用、类继承、for、if后，再阅读本系列教程。  
## 博客
博客简单来说，就类似于记事本、日记、长篇微博、QQ空间之类的网站。  
不过，它的后台和前端页面都是我们自己手写的。  
如果你有打开上面的项目的源码进行浏览，会发现templates目录下的blog_list.html和blog_detail.html里面的代码也就几句话，直接使用浏览器打开的话只是几个`{{ xxxx }}`  
而我们运行项目并打开[http://localhost:8000/django-1](http://localhost:8888/django-1),却可以看到本篇博文。  
这是为什么呢？？  
继续浏览后面并动手的话，你就会知道为什么了。  
