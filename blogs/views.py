from django.shortcuts import render
from .models import Blog_Topic, Blog_Entry, Blog_Comment


# home page.
def index(request):
    return render(request, 'blogs/index.html')


def blog_topics(request):
    # shows all blog topics
    blog_topics = Blog_Topic.objects.all()
    context = {'blog_topics': blog_topics}
    return render(request, 'blogs/blog_topics.html', context)


def blogs(request, blog_topic_id):
    # show blogs for topic
    blog_topic = Blog_Topic.objects.get(id=blog_topic_id)
    blogs = blog_topic.blog_entry_set.order_by('-date_added')
    context = {'blog_topic': blog_topic, 'blogs': blogs}
    return render(request, 'blogs/blogs.html', context)


def blog(request, blog_entry_id):
    # show blog and comments
    blog_entry = Blog_Entry.objects.get(id=blog_entry_id)
    blog_topic = blog_entry.topic
    comments = blog_entry.blog_comment_set.order_by('-date_added')
    context = {'blog_topic': blog_topic, 'blog_entry': blog_entry, 'comments': comments}

    return render(request, 'blogs/blog.html', context)
