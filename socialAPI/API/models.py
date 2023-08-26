

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    MEDIA_TYPES = [
        ('text', 'Text'),
        ('image', 'Image'),
        ('video', 'Video'),
    ]
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPES)
    media_url = models.URLField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Interaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    INTERACTION_TYPES = [
        ('like', 'Like'),
        ('comment', 'Comment'),
        ('share', 'Share'),
    ]
    interaction_type = models.CharField(max_length=10, choices=INTERACTION_TYPES)
    timestamp = models.DateTimeField(auto_now_add=True)

class Group(models.Model):
    group_name = models.CharField(max_length=100)
    description = models.TextField()

class GroupMembership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    join_date = models.DateTimeField(auto_now_add=True)


class Follower(models.Model):
    follower = models.ForeignKey(User, related_name='following_relations', on_delete=models.CASCADE)
    following = models.ForeignKey(User, related_name='followers_relations', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

class Following(models.Model):
    follower = models.ForeignKey(User, related_name='followed_by_relations', on_delete=models.CASCADE)
    following = models.ForeignKey(User, related_name='following_to_relations', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Reply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, related_name='replies', on_delete=models.CASCADE)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Follow(models.Model):
    follower = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    following = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.follower.username} follows {self.following.username}"


class Unfollow(models.Model):
    unfollower = models.ForeignKey(User, related_name='unfollowing_relations', on_delete=models.CASCADE)
    unfollowing = models.ForeignKey(User, related_name='unfollowers_relations', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
