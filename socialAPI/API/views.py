from rest_framework import generics, viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response 
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .serializers import *
from .models import *


class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if self.object:
            token, created = Token.objects.get_or_create(user=self.object)
            response.data['token'] = token.key
        return response

class UserLoginView(generics.CreateAPIView):
    serializer_class = UserLoginSerializer

    def create(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': 'Invalid credentials'}, status=400)
        


class UserProfileView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
       
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        post_id = request.data.get('post_id')
        user = request.user

        try:
            post = Post.objects.get(pk=post_id)
        except Post.DoesNotExist:
            return Response({'error': 'Post not found'}, status=404)

        like, created = Interaction.objects.get_or_create(
            user=user,
            post=post,
            interaction_type='like'
        )

        if created:
            serializer = LikeSerializer(like)
            return Response(serializer.data, status=201)
        else:
            return Response({'error': 'Already liked'}, status=400)

class SharePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        post_id = request.data.get('post_id')
        user = request.user

        try:
            post = Post.objects.get(pk=post_id)
        except Post.DoesNotExist:
            return Response({'error': 'Post not found'}, status=404)

        share, created = Interaction.objects.get_or_create(
            user=user,
            post=post,
            interaction_type='share'
        )

        if created:
            serializer = ShareSerializer(share)
            return Response(serializer.data, status=201)
        else:
            return Response({'error': 'Already shared'}, status=400)

class FollowUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        following_id = request.data.get('following_id')
        user = request.user

        try:
            following = User.objects.get(pk=following_id)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=404)

        follow, created = Follow.objects.get_or_create(
            follower=user,
            following=following
        )

        if created:
            serializer = FollowSerializer(follow)
            return Response(serializer.data, status=201)
        else:
            return Response({'error': 'Already following'}, status=400)

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

class ReplyViewSet(viewsets.ModelViewSet):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer
    permission_classes = [permissions.IsAuthenticated]



class FollowerViewSet(viewsets.ModelViewSet):
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer




class CommentPostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        post_id = request.data.get('post_id')
        text = request.data.get('text')
        user = request.user

        try:
            post = Post.objects.get(pk=post_id)
        except Post.DoesNotExist:
            return Response({'error': 'Post not found'}, status=404)

        comment = Comment.objects.create(user=user, post=post, text=text)
        serializer = CommentSerializer(comment)
        return Response(serializer.data, status=201)


class ReplyCommentView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        comment_id = request.data.get('comment_id')
        text = request.data.get('text')
        user = request.user

        try:
            comment = Comment.objects.get(pk=comment_id)
        except Comment.DoesNotExist:
            return Response({'error': 'Comment not found'}, status=404)

        reply = Reply.objects.create(user=user, comment=comment, text=text)
        serializer = ReplySerializer(reply)
        return Response(serializer.data, status=201)    


class FollowerViewSet(viewsets.ModelViewSet):
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer

class FollowingViewSet(viewsets.ModelViewSet):
    queryset = Following.objects.all()
    serializer_class = FollowingSerializer



class SharePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        post_id = request.data.get('post_id')
        user = request.user

        try:
            post = Post.objects.get(pk=post_id)
        except Post.DoesNotExist:
            return Response({'error': 'Post not found'}, status=404)

        share, created = Interaction.objects.get_or_create(
            user=user,
            post=post,
            interaction_type='share'
        )

        if created:
            serializer = ShareSerializer(share)
            return Response(serializer.data, status=201)
        else:
            return Response({'error': 'Already shared'}, status=400)    
        

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class GroupMembershipViewSet(viewsets.ModelViewSet):
    queryset = GroupMembership.objects.all()
    serializer_class = GroupMembershipSerializer    



class FollowerViewSet(viewsets.ModelViewSet):
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer

class FollowingViewSet(viewsets.ModelViewSet):
    queryset = Following.objects.all()
    serializer_class = FollowingSerializer        

