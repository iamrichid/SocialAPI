from django.contrib import admin
from .models import Post, Interaction, Group, GroupMembership, Follower, Following, Comment, Reply

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'media_type', 'timestamp')

@admin.register(Interaction)
class InteractionAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'interaction_type', 'timestamp')

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('group_name', 'description')

@admin.register(GroupMembership)
class GroupMembershipAdmin(admin.ModelAdmin):
    list_display = ('user', 'group', 'join_date')

@admin.register(Follower)
class FollowerAdmin(admin.ModelAdmin):
    list_display = ('follower', 'following', 'timestamp')

@admin.register(Following)
class FollowingAdmin(admin.ModelAdmin):
    list_display = ('follower', 'following', 'timestamp')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'text', 'timestamp')

@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    list_display = ('user', 'comment', 'text', 'timestamp')
