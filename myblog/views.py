from django.shortcuts import render
from django.views import View
from myblog.models import Blog, Category, Link, About
from pure_pagination import PageNotAnInteger, Paginator
import markdown
# Create your views here.
class Index(View):
    """
    博客首页
    """
    def get(self, request):
        all_blog = Blog.objects.all().order_by('-id')
        top_blog = Blog.objects.filter(top=1).order_by('-id')

        #分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_blog, 8, request=request)  #每页显示
        all_blog = p.page(page)

        return render(request, 'index.html', {'all_blog': all_blog, 'top_blog': top_blog})

class BlogPage(View):
    """
    博客详情页
    """
    def get(self, request, blog_id):
        blog = Blog.objects.get(id=blog_id)
        blog_content = markdown.markdown(blog.content.replace("\r\n", '  \n'), extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
        ], safe_mode=True, enable_attributes=False)
        # 博客点击数+1, 评论数统计
        blog.click_nums += 1
        blog.save()
        # 实现博客上一篇与下一篇功能
        has_prev = False
        has_next = False
        id_prev = id_next = int(blog_id)
        blog_id_max = Blog.objects.all().order_by('-id').first()
        id_max = blog_id_max.id
        while not has_prev and id_prev >= 1:
            blog_prev = Blog.objects.filter(id=id_prev - 1).first()
            if not blog_prev:
                id_prev -= 1
            else:
                has_prev = True
        while not has_next and id_next <= id_max:
            blog_next = Blog.objects.filter(id=id_next + 1).first()
            if not blog_next:
                id_next += 1
            else:
                has_next = True

        return render(request, 'blogpage.html', {
            'blog': blog,
            'blog_prev': blog_prev,
            'blog_next': blog_next,
            'has_prev': has_prev,
            'has_next': has_next,
            'blog_content': blog_content,
        })

class CategoryIndex(View):
    """
    分类页面
    """
    def get(self, request):
        all_category = Category.objects.all().order_by('id')

        return render(request, 'categoryindex.html', {'all_category': all_category})

class CategoryPage(View):
    """
    分类详情页面
    """
    def get(self, request, category_name):
        category = Category.objects.filter(name=category_name).first()
        cate_blogs = category.blog_set.all().order_by('-id')

        return render(request, 'category.html', {
            'cate_blogs': cate_blogs,
            'category_name': category_name,
        })

class LinkPage(View):
    """
    友链
    """
    def get(self, request):
        link = Link.objects.all()
        for link_content in link:
            link_content = markdown.markdown(link_content.content.replace("\r\n", '  \n'), extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
                'markdown.extensions.toc',
            ], safe_mode=True, enable_attributes=False)

        return render(request, 'link.html', {'link_content': link_content})

class AboutPage(View):
    """
    关于
    """
    def get(self, request):
        about = About.objects.all()
        for about_content in about:
            about_content = markdown.markdown(about_content.content.replace("\r\n", '  \n'), extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
                'markdown.extensions.toc',
            ], safe_mode=True, enable_attributes=False)

        return render(request, 'about.html', {'about_content': about_content})
