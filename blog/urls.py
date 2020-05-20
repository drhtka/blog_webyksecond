# -*- coding: utf-8 -*-
"""
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
#from django.contrib.auth import views

from blog.views import IndexTemplateView, PostListView, MainView

urlpatterns = [

    url(r'^index/', IndexTemplateView.as_view(), name='index'),
    url(r'^postlist/', PostListView.as_view(), name='postlist'),
    #url(r'^', MainView.as_view(), name='main'),
    #url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    #url(r'^login/$', views.LoginView.as_view(), name='login'),
]
