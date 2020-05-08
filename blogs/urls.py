""" Defines URL patterns for blogs. """
from django.urls import path

from . import views


app_name = 'blogs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # View Topic page for blogs
    path('blog_topics/', views.blog_topics, name='blog_topics'),
    # View Blogs for the topic
    path('blogs/<int:blog_topic_id>/', views.blogs, name='blogs'),
    # View individual blog and comments
    path('blog/<int:blog_entry_id>/', views.blog, name='blog'),
    # Create new blog Topic
    path('new_blog_topic/', views.new_blog_topic, name='new_blog_topic'),
]