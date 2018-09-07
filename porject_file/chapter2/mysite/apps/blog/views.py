from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Blog,BlogTag,BlogType
# Create your views here.

# 分页通用函数，第一个参数是内容列表，第二个参数是页码
def page_gen(contact_list,page):
    # 分页规则 ，第一个参数，内容列表，第二个参数，每页多少内容。第三个参数，孤儿参数
    # 孤儿参数： 假如现在总共有12篇博文，正常来说每页有10篇博文，那么总页码应该有两页。
    # 但采取了孤儿参数后，第一页会有12篇博文，没有了第二页。
    # 除非有13篇博文，才会出现第二页
    paginator = Paginator(contact_list, 10,2)
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # 如果传入的参数不是整数类型，返回第一页内容
        # 假如用户输入page=abcd或者其他字符，返回第一页内容
        contacts = paginator.page(1)
    except EmptyPage:
        # 如果传入的页码大于最大的页码数，返回最后一页的内容
        # 现在总共有5页，如果用户输入第6页则返回第5页的内容
        contacts = paginator.page(paginator.num_pages)

    return contacts

# 首页
def home(request):
    return render(request,'home.html')

# 所有博客列表
def blog_list(request):
    context = {}

    contact_list = Blog.objects.all()
    # 从请求中查找是否有page参数，如果有则取page的参数
    # 没有则取1
    page = request.GET.get('page',1)

    context['blogs'] = page_gen(contact_list,page)

    return render(request, 'blog_list.html', context)


# 按标签分类的博客列表
def blog_tag(request, slug):
    context = {}
    # 在BlogTag中也就是我们的数据库中寻找有没有slug字段和传进来的slug字段匹配的
    blog_tag = get_object_or_404(BlogTag, slug=slug)

    # 从Blog中寻找是在该标签下的文章列表
    contact_list = Blog.objects.filter(blog_tag=blog_tag)

    page = request.GET.get('page', 1)
    # 从请求中查找是否有page参数，如果有则取page的参数
    # 没有则取1
    context['blogs'] = page_gen(contact_list, page)


    return render(request, 'blog_tag.html', context)

def blog_type(request, slug):
    context = {}
    # 在BlogTag中也就是我们的数据库中寻找有没有slug字段和传进来的slug字段匹配的
    blog_type = get_object_or_404(BlogType, slug=slug)

    # 从Blog中寻找是在该标签下的文章列表
    contact_list = Blog.objects.filter(blog_type=blog_type)

    page = request.GET.get('page', 1)
    # 从请求中查找是否有page参数，如果有则取page的参数
    # 没有则取1
    context['blogs'] = page_gen(contact_list, page)

    return render(request, 'blog_type.html', context)


def blog_detail(request,slug): # 接收请求和slug参数
    context = {}  # 生成一个空字典

    # 在Blog也就是我们的数据库中寻找有没有slug字段和传进来的slug字段匹配的
    # 没有，则返回404,有则返回该对象的内容
    context['blog'] = get_object_or_404(Blog, slug=slug)
    # blog_detail.html未创建
    return render(request,'blog_detail.html',context)
