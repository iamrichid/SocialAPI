from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *


# Create a router and register viewsets
router = DefaultRouter()
router.register(r'groups', GroupViewSet)
router.register(r'group-memberships', GroupMembershipViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'replies', ReplyViewSet)
router.register(r'followers', FollowerViewSet)
router.register(r'following', FollowingViewSet)

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('posts/', PostViewSet.as_view({'get': 'list', 'post': 'create'}), name='post-list'),
    path('posts/<int:pk>/', PostViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='post-detail'),
    path('posts/<int:pk>/like/', LikePostView.as_view(), name='post-like'),
    path('posts/<int:pk>/share/', SharePostView.as_view(), name='post-share'),
    path('follow/', FollowUserView.as_view(), name='follow-user'),
    path('comments/post/', CommentPostView.as_view(), name='comment-post'),
    path('replies/comment/', ReplyCommentView.as_view(), name='reply-comment'),
    path('', include(router.urls)),
]

