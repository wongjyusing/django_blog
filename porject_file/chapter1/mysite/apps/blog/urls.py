# 从django的路由方法导入 路径、正则路径方法
from django.urls import path,re_path
# 从当前目录下导入views.py的内容
from . import views

urlpatterns = [
    # 下面方法中第一个参数是路径
    # 总路由也是为空，所以我们的博客列表就是首页
    # 当我们在浏览器打开 http://127.0.0.1:8000
    # 就会发送一个请求给django
    # django就会从路由器中寻找是否有这路径的，没有就会返回404
    # 有就寻找该路径对应的方法，也就是下面的第二个参数，
    # 第三个参数，相当于是变量名，也就是说 blog_list = path('', views.blog_list)
    # 后面使用模板时会用到，现在知道一下就好了
    path('', views.blog_list,name='blog_list'),

    # re_path不难理解是正则匹配路径
    # 大家可以回头看一下views.py中的blog_detail函数
    # 它除了request参数还有一个slug参数
    # 解释一下这里的正则表达式吧：
    # 这是正则表达式匹配路径，/(?P<slug>[\w-]+)/
    # 以/开头 以/结束  括号()是括起来的的表达式作为一个分组
    # [\w-]是匹配任意字母数字和减号
    # (?P<slug>[\w-]+)就是把slug进行分组，匹配里面的[\w-]
    re_path('detail/(?P<slug>[\w-]+)/', views.blog_detail, name='detail'),
]
