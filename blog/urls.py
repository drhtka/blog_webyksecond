# -*- coding: utf-8 -*-
"""
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from blog.views import IndexTemplateView, PostListView

urlpatterns = [
    url(r'^index/', IndexTemplateView.as_view(), name='index'),
    url(r'^postlist/', PostListView.as_view(), name='postlist'),
]
