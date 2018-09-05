# 从Django的快捷方法中导入 渲染、要么获取对象要么404方法
from django.shortcuts import render,get_object_or_404
# 从当前目录下的models.py中导入Blog类
from .models import Blog

# 所有博客列表方法 首页的处理方法
def blog_list(request):
    context = {}   # 生成一个空字典
    context['blogs'] = Blog.objects.all() # 获取Blog中的所有对象

    # request 请求 意思是当我们在浏览器中访问 http://127.0.0.1:8000
    # 就相当于发送了一个请求给Django，当请求成功后
    # django就把context的内容在blog_list.html中渲染并返回给这个请求。
    # blog_list.html在后面环节再创建
    return render(request,'blog_list.html',context)

# 文章详情页内容的处理方法
def blog_detail(request,slug): # 接收请求和slug参数
    context = {}  # 生成一个空字典

    # 在Blog也就是我们的数据库中寻找有没有slug字段和传进来的slug字段匹配的
    # 没有，则返回404,有则返回该对象的内容
    context['blog'] = get_object_or_404(Blog, slug=slug)
    # blog_detail.html未创建
    return render(request,'blog_detail.html',context)
