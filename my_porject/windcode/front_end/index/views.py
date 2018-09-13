from django.shortcuts import render

# 首页
def home(request):
    return render(request,'home.html')

# 博客列表页
def blog_list(request):
    return render(request,'blog_list.html')
