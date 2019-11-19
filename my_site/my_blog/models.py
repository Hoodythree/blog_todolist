from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Blog_Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Blog_Tag(models.Model):
    name = models.CharField(max_length=200)

    # 过滤器 : 获取某一个tag下的文章数量
    def get_tag_post_sum(self):
        posts = Blog_Post.objects.filter(pk=self.id)
        return len(posts)

    def __str__(self):
        return self.name


class Blog_Post(models.Model):

    title = models.CharField(max_length=200)

    body = models.TextField()

    create_time = models.DateTimeField()

    update_time = models.DateTimeField()

    abstract = models.CharField(max_length=200, blank=True)

    category = models.ForeignKey(Blog_Category, on_delete=models.CASCADE)

    tag = models.ManyToManyField(Blog_Tag, blank=True)

    blog_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

#     自定义get_url方法,生成url
    def get_absolute_url(self):
        return reverse('my_blog:detail', kwargs={'pk': self.pk})



