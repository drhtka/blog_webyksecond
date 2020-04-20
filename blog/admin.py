# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.models import User
from blog.models import Blogs

class BlogAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'created', 'status', 'subscribe')
    list_filter = ('author', 'status', 'subscribe')
    raw_id_fields = ('author',)
    ordering = ('created',)

admin.site.register(Blogs, BlogAdmin)