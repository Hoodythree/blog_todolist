from django.shortcuts import render, get_object_or_404
from .models import Blog_Post, Blog_Tag, Blog_Category
import markdown
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# def home(request):
#     post_list = Blog_Post.objects.all().order_by('-create_time')
#
#     tag_list = Blog_Tag.objects.all()
#
#     return render(request, 'my_blog/index.html', {'post_list': post_list, 'tag_list': tag_list})
def home(request):
    post_lists = Blog_Post.objects.all().order_by('-create_time')

    tag_list = Blog_Tag.objects.all()

    paginator = Paginator(post_lists, 3)

    page = request.GET.get('page')

    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)
    return render(request, 'my_blog/index.html', {'post_list': post_list, 'tag_list': tag_list, 'post_lists': post_lists})


# 文章详情
def detail(request, pk):
    post = get_object_or_404(Blog_Post, pk=pk)

    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    return render(request, 'my_blog/blog.html', {'post': post})


def archive(request):
    post_list = Blog_Post.objects.all()
    return render(request, 'my_blog/archives.html', {'post': post_list})


def tags(request):
    tag_list = Blog_Tag.objects.all()
    return render(request, 'my_blog/tags.html', {'tags': tag_list})


def types(request):
    type_list = Blog_Category.objects.all()
    return render(request, 'my_blog/types.html', {'types': type_list})


def tags_posts(request, pk):
    tag = get_object_or_404(Blog_Tag, pk=pk)
    blog_list = Blog_Post.objects.filter(tag=tag)
    tag_list = Blog_Tag.objects.all()
    return render(request, 'my_blog/tags.html', {'blog_list': blog_list, 'tags': tag_list})


def types_posts(request, pk):
    blog_type = get_object_or_404(Blog_Category, pk=pk)
    blog_list = Blog_Post.objects.filter(category=blog_type)
    type_list = Blog_Category.objects.all()
    return render(request, 'my_blog/types.html', {'blog_list': blog_list, 'types': type_list})


def search(request):
    q = request.GET.get('q')

    print(q)
    error_msg = ''

    if not q:
        error_msg = '请输入关键词'
        return render(request, 'my_blog/index.html', {'error_msg': error_msg})

    post_list = Blog_Post.objects.filter(title__icontains=q)
    return render(request, 'my_blog/index.html', {'error_msg': error_msg, 'post_list': post_list})
