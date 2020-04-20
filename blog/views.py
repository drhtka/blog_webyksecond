# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone
from django.views.generic import ListView, TemplateView, View
from django.views.generic.edit import CreateView
# from django.views.generic.base import View
#from blogs.forms import BlogPostsForms
from blog.models import Blogs
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
# Create your views here.

class IndexTemplateView(LoginRequiredMixin, TemplateView):
    #  стартовая траница со всами постами всех зарегестированных пользователей
    def get(self, request):
        template_name = 'blog/index.html'
        all_posts = Blogs.objects.all()
        context = {'all_posts': all_posts}
        return render(request, template_name, context)

class PostListView(LoginRequiredMixin, ListView):
    #  страница со всами постами зарегестированного пользователя
    model = Blogs
    context_object_name = "posts"
    template_name = 'blog/details.html'
    login_url = 'login'

    def get_qetyset(self):
        u = self.request.user
        qs = super().get_queryset()
        return qs.filter(author=u)