from django.contrib import admin
from myblog.models import Blog, Category, Link, About

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'click_nums', 'category', 'top', 'create_time']

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)
admin.site.register(Link)
admin.site.register(About)
