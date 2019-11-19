from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView

post = [
    {
        'author': 'Chris',
        'title': 'Strong Body',
        'content': 'best practice for body shape',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Paul',
        'title': 'Nba revolution',
        'content': 'Today, We fight',
        'date_posted': 'August 27, 2019'
    }
]


def home(request):
    context = {
        'post': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


# 使用通用视图模板
# 不需要显式地从数据库取值
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'post'
    # 排序
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    # 排序
    ordering = ['-date_posted']


def about(request):
    return render(request, 'blog/about.html')

