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

class MainView(TemplateView):
    #  стартовая траница для не зарегстрированных

    template_name = 'blog/main.html'

class IndexTemplateView(LoginRequiredMixin, TemplateView):
    #  стартовая страница со всами постами всех зарегестированных пользователей
    def get(self, request):
        template_name = 'blog/index.html'
        all_posts = Blogs.objects.all()

        context = {'all_posts': all_posts}
        print(all_posts)
        return render(request, template_name, context)

class PostListView(LoginRequiredMixin, ListView):
    #  страница со всеми постами зарегестированного пользователя
    model = Blogs
    context_object_name = "posts"
    template_name = 'blog/details.html'
    login_url = 'login'
    print('qs')
    def get_qetyset(self):
        u = self.request.user
        print(u)
        print('u')
        qs = super().get_queryset()
        print(qs)
        return qs.filter(author=u)

class AddTestView(LoginRequiredMixin, TemplateView):
    pass