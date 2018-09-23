from django.conf.urls import url

from blog.views import *


app_name = 'blog'
urlpatterns = [
    url(r'^list/$', BlogListView.as_view(), name="blog-list"),
    url(r'^list/(?P<slug>[\w\\-]+)/$', TagBlogListView.as_view(), name="blog-tag-list"),
    url(r'^list/(?P<year>[0-9]+)/(?P<month>[0-9]+)/$', MonthBlogListView.as_view(), name="blog-month-list"),
    url(r'^write/$', BlogCreateView.as_view(), name='blog-create'),
    url(r'^(?P<slug>[\w\\-]+)/$', BlogDetailView.as_view(), name="blog-detail"),
]