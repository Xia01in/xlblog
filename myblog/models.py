from django.db import models
from datetime import datetime
from mdeditor.fields import MDTextField

# Create your models here.
class Category(models.Model):
    """
    文章分类
    """
    name = models.CharField(verbose_name='文章类别', max_length=20)

    class Meta:
        verbose_name = '文章类别'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name

class Blog(models.Model):
    """
    博客设计
    """
    title = models.CharField(verbose_name='标题', max_length=100)
    content = MDTextField(verbose_name='文章内容')
    create_time = models.DateTimeField(verbose_name='发布时间', default=datetime.now)
    click_nums = models.IntegerField(verbose_name='点击量', default=0)
    category = models.ForeignKey(Category, blank=True, null=True, verbose_name='文章分类', on_delete=models.CASCADE)
    top = models.BooleanField(default=False, verbose_name='是否置顶')

    class Meta:
        verbose_name = '我的博客'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.title

class Link(models.Model):
    """
    友链
    """
    content = MDTextField(verbose_name='内容')

    class Meta:
        verbose_name = '友链'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.content

class About(models.Model):
    """
    关于
    """
    content = MDTextField(verbose_name='内容')

    class Meta:
        verbose_name = '关于'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.content