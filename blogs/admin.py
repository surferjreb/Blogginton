from django.contrib import admin
from .models import Blog_Topic, Blog_Entry, Blog_Comment


# Register your models here.
admin.site.register(Blog_Topic)
admin.site.register(Blog_Entry)
admin.site.register(Blog_Comment)
