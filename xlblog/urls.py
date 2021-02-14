"""xlblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from myblog.views import Index, BlogPage, CategoryPage, CategoryIndex, LinkPage, AboutPage
from django.conf import settings
from django.views import static

urlpatterns = [
    path('admin/', admin.site.urls),  #后台地址
    path('', Index.as_view(), name='index'),  #首页
    path('category/', CategoryIndex.as_view(), name='category'),  #总分类
    path('link/', LinkPage.as_view(), name='link'),  #友链
    path('about/', AboutPage.as_view(), name='about'),  #关于
    path('blog/<blog_id>', BlogPage.as_view(), name='blog_id'),  #文章页面
    path('category/<category_name>', CategoryPage.as_view(),  name='category_name'),  #单个分类
    # 后台 markdown 编辑器配置
    path('mdeditor/', include('mdeditor.urls')),
    path('static/<path>', static.serve, {'document_root': settings.STATIC_ROOT }, name='static'),  #静态文件
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# 设置后台名称
admin.site.site_header = 'xlblog博客后台'
admin.site.site_title = 'xlblog后台'
