from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django.utils.timezone import now
# User=get_user_model()
# Create your models here.


class NewPost(models.Model):
    id = models.BigAutoField(primary_key=True)

    Author = models.ForeignKey(User, on_delete=models.CASCADE)
    Title = models.CharField(max_length=264)
    Text = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True, null=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.Title

    def get_absolute_url(self):
        return reverse("blogapp:view_draft", kwargs={'pk': self.pk})

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    # def get_absolute_url(self):
    #     return reverse("blogapp:drafts", kwargs={'pk':self.pk})


class Comment(models.Model):
    post = models.ForeignKey(
        NewPost, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
