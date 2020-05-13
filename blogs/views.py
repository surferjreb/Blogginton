from django.shortcuts import render, redirect
from .models import Blog_Topic, Blog_Entry, Blog_Comment
from .forms import BlogTopicForm, BlogEntryForm


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


def new_blog_topic(request):
    # Add a new blog topic
    if request.method != 'POST':
        # No data submitted
        form = BlogTopicForm()
    else:
        # POST data submitted and process data
        form = BlogTopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blog_topics')

    # Display blank form.
    context = {'form': form}
    return render(request, 'blogs/new_blog_topic.html', context)


def new_blog_entry(request, blog_topic_id):
    # add a new entry to a blog topic
    blog_topic = Blog_Topic.objects.get(id=blog_topic_id)

    if request.method != 'POST':
        # no data submitted
        form = BlogEntryForm()
    else:
        # POST method used to submit data
        form = BlogEntryForm(data=request.POST)
        if form.is_valid():
            new_blog_entry = form.save(commit=False)
            new_blog_entry.blog_topic = blog_topic
            new_blog_entry.save()
            return redirect('blogs:blogs', blog_topic_id=blog_topic_id)

    # Display blank form
    context = {'blog_topic': blog_topic, 'form': form}
    return render(request, 'blogs/new_blog_entry.html', context)


def edit_blog_entry(request, blog_entry_id):
    # Edit an existing blog entry
    blog_entry = Blog_Entry.objects.get(id=blog_entry_id)
    blog_topic = blog_entry.topic

    if request.method != 'POST':
        # Initial request
        form = BlogEntryForm(instance=blog_entry)
    else:
        # POst data submitted
        form = BlogEntryForm(instance=blog_entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blogs', blog_topic_id=blog_topic.id)

    # display blank form
    context = {'blog_entry': blog_entry, 'blog_topic': blog_topic, 'form': form}
    return render(request, 'blogs/edit_blog_entry.html', context)
