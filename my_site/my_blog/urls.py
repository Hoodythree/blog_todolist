from django.urls import path
from . import views

app_name = 'my_blog'
urlpatterns = [
    path('', views.home, name='my-blog-home'),
    path('search/', views.search, name='search'),
    path('posts/<pk>/', views.detail, name='detail'),
    path('archives/', views.archive, name='archive'),
    path('tags/', views.tags, name='tags'),
    path('tags/<pk>', views.tags_posts, name='tags_posts'),
    path('types/', views.types, name='types'),
    path('types/<pk>', views.types_posts, name='types_posts'),
]