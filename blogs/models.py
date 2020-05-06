from django.db import models


# Create your models here.

class Blog_Topic(models.Model):
    text = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.text}'


class Blog_Entry(models.Model):
    topic = models.ForeignKey(Blog_Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.text[:50]}...'


class Blog_Comment(models.Model):
    blog = models.ForeignKey(Blog_Entry, on_delete=models.CASCADE)
    text = models.TextField(max_length=180)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.text}'

# add a way for users to comment on comments
# and be able to link other comments without reposting