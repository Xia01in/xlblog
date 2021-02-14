## xlblog

基于Django框架编写的博客系统。

展示：[本人博客](https://llwxx.top)

前端：[https://github.com/sanjinhub/hexo-theme-geek](https://github.com/sanjinhub/hexo-theme-geek)

后台：[https://github.com/newpanjing/simpleui](https://github.com/newpanjing/simpleui)

系统：CentOS  8.0 64位

## 功能

由于本人太菜，该系统就只有一些博客基本的功能，当然也因为我想让博客看起来更简洁一点，所以评论系统就没用，我看这个前端原来用的是[Valine](https://valine.js.org/)，需要评论系统的可以自己动手加上或者自己写一个。

- 首页分页功能
- 文章分类功能
- 友链和关于页面
- 文章置顶功能
- 分类归档页面
- 文章内上文切换功能
- 后台markdown实时预览功能
- 黑白模式切换功能

## 运行

##### 安装所需的库：

`pip3 install -r requirements.txt`

##### 连接数据库创建数据：

`python3 manage.py migrate`

##### 收集静态文件：

`python3 manage.py collectstatic`

##### 创建后台root登录用户：

`python3 manage.py createsuperuser`

##### uWSGI运行系统：

`uwsgi --ini uwsgi.ini`

##### 访问：

首页：[localhost:8000](localhost:8000)

后台：[localhost:8000/admin](localhost:8000/admin)（后台地址可以通过xlblog目录下的urls.py文件修改）

##### 注意：

①第一次运行，没有在后台创建友链和关于页面的话，在前端访问是会报错的。

②首页头像和网站icon在static和static/img目录下修改。

③网页名字、首页名字和个性签名是在templates目录下的各个html文件中写死的，可以根据需要自行修改。