from django.contrib import admin
from .models import Blog_Post, Blog_Category, Blog_Tag

admin.site.register(Blog_Post)
admin.site.register(Blog_Category)
admin.site.register(Blog_Tag)
# Register your models here.
