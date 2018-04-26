from django.contrib.auth.models import User
from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from project.feed.models import Post, Like, UserProfile, FriendRequest
from project.api.serializers import FeedDisplaySerializer, PostSerializer, UserSerializer, \
    UserProfileSerializer, FriendsViewSerializer


# This class displays the Feed under api/feed/
class FeedDisplayView(APIView):
    permission_classes = [
        IsAuthenticated,
    ]

    def get(self, request, format=None):
        search = request.query_params.get('search')
        if search:
            posts = Post.objects.filter(content__contains=search)
        else:
            posts = Post.objects.all()
        serializer = FeedDisplaySerializer(posts, many=True)
        return Response(serializer.data)


class UserDisplayView(APIView):
    permission_classes = [
        IsAuthenticated,
    ]

    def get(self, request, user_id, format=None):
        posts = Post.objects.all()
        data = []
        for post in posts:
            if user_id == post.user_id:
                data.append({
                    'id': post.id,
                    'content': post.content,
                    'created': post.created,
                    'user': {
                        'id': post.user.id,
                        'username': post.user.username,
                        'post_count': post.user.posts.count(),
                        'fame_index': sum([p.likes.count() for p in post.user.posts.all()]),
                    }
                })
        serializer = FeedDisplaySerializer(data=data, many=True)
        return Response(serializer.initial_data)


class ListLikedPostsView(APIView):
    permission_classes = [
        IsAuthenticated,
    ]

    def get_stupid(self, request):
        likes = Like.objects.filter(user=request.user)
        posts = [l.post for l in likes]
        return Response(PostSerializer(posts, many=True).data)


class PostGetUpdateDeleteView(APIView):
    permission_classes = [
        IsAuthenticated,
    ]

    def get_object(self, post_id):
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            raise Http404
        return post

    def get(self, request, post_id):
        post = self.get_object(post_id)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def post(self, request, post_id):
        post = self.get_object(post_id)
        serializer = PostSerializer(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, post_id):
        post = self.get_object(post_id)
        post.delete()
        return Response('OK')


class PostCreateView(APIView):
    permission_classes = [
        IsAuthenticated,
    ]

    def post(self, request):
        serializer = PostSerializer(
            data=request.data,
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        post = serializer.create(request.data)
        post.save()
        return Response(PostSerializer(post).data)


class LikeView(APIView):
    permission_classes = [
        IsAuthenticated,
    ]

    def get(self, request):
        user = request.user
        Likes = Like.objects.all()
        like_list = [l for l in Likes if user == l.user]
        return Response(len(like_list))

    def post(self, request, post_id):
        postz = Post.objects.get(id=post_id)
        like = Like.objects.create(
            user=request.user,
            post=postz
        )
        like.save()
        return Response('OK!')


class SharePostView(APIView):

    def post(self, request, post_id):
        user = request.user
        try:
            Post.objects.get(post_id)
        except Exception:
            raise Http404
        new_post = Post.objects.create(
            user=user,
            content='',
            share_relation=post_id
        )
        new_post.save()
        return Response('Post shared (new Post created)')


class FollowingView(APIView):
    permission_classes = [
        IsAuthenticated,
    ]

    def get_object(self, user_id):
        try:
            return User.object.get(id=user_id)
        except User.DoesNotExist:
            raise Http404

    def post(self, request, user_id):
        user = User.objects.get(id=user_id)
        my_user = request.user
        user_profile, created = UserProfile.objects.get_or_create(user=my_user)
        user_profile.followees.add(user)
        return Response('OK')

    def get(self, request):
        serializer = UserSerializer(
            [u.user for u in request.user.followers.all()], many=True
        )
        return Response(serializer.data)


class TokenView(APIView):
    permission_classes = [
        IsAuthenticated,
    ]

    def get(self, request):
        return 'Alicia Silverstone'


class allPostSearchView(APIView):
    permission_classes = [
        IsAuthenticated,
    ]

    def get_object(self, post_id):
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            raise Http404
        return post

    def get(self, search_string):
        self.get_object(search_string)
        return Post.get_objects.filter(content__contains=search_string)


class DislikeView(APIView):
    permission_classes = [
        IsAuthenticated,
    ]

    def get(self, request):
        user = request.user
        Likes = Like.objects.all()
        like_list = [l for l in Likes if user == l.user]
        return Response(len(like_list))

    def post(self, request, post_id):
        postz = Post.objects.get(id=post_id)

        like = Like.objects.filter(
            post=postz
        )
        like.delete()
        return Response('Post Deleted!')


class UserProfileView(APIView):
    permission_classes = [
        IsAuthenticated,
    ]

    def get(self, request):
        up = UserProfile.objects.get(user=request.user)
        return Response(UserProfileSerializer(up).data)

    def post(self, request):
        up = UserProfile.objects.get(user=request.user)
        serializer = UserProfileSerializer(up, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(UserProfileSerializer(up).data)


class FriendsDeleteView(APIView):
    permission_classes = [
        IsAuthenticated,
    ]

    def post(self, request):
        try:
            friendship = FriendRequest.objects.filter(friend_user=request.user, STATUS='ACCEPTED')
            friendship.delete()
        except:
            friendship = FriendRequest.objects.filter(my_user=request.user, STATUS='ACCEPTED')
            friendship.delete()
        return "Friendship deleted..."


class FriendsRequestMyView(APIView):
    def get(self, request):
        friend_requests = FriendRequest.objects.filter(friend_user=request.user, STATUS='PENDING')
        serializer = FriendsViewSerializer(friend_requests, many=True)
        return Response(serializer.data)


class FriendsRequestGeneralView(APIView):
    permission_classes = [
        IsAuthenticated,
    ]

    def get(self, request):
        serializer = FriendsViewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)

    def post(self, request, user_id):
        try:
            friend_user = User.objects.get(id=user_id)
        except:
            raise Http404

        friend_request = FriendRequest.objects.create(my_user=request.user, friend_user=friend_user)
        return Response(FriendsViewSerializer(friend_request).data)


class FriendsRequestStatusAccept(APIView):
    permission_classes = [
        IsAuthenticated,
    ]

    def post(self, request, request_id):
        try:
            friend_request = FriendRequest.objects.get(id=request.user, friend_user=request_id, STATUS='PENDING')
        except:
            return Response("Can't find the user!")
        friend_request.STATUS = 'ACCEPTED'
        friend_request.save()
        return Response(FriendsViewSerializer(friend_request).data)

class FriendsRequestStatusReject(APIView):
    permission_classes = [
        IsAuthenticated,
    ]

    def post(self, request_id):
        friend_request = FriendRequest.objects.filter(friend_user=request_id, STATUS='PENDING')
        if friend_request == '{}':
            return 'No pending friend requests!'
        friend_request.STATUS = 'REJECTED'
        friend_request.save()
        return Response('Friendship rejected!')


class FriendsSimplePostView(APIView):
    permission_classes = [
        IsAuthenticated,
    ]

    def get(self, request):
        user = request.user
        my_friends = FriendRequest.objects.filter(friend_user=user)
        serializer = FriendsViewSerializer(data=request.user)
        posts = my_friends.friend_user.posts
        return Response(serializer(posts).data)

class FriendsSimpleView(APIView):
    permission_classes = [
        IsAuthenticated,
    ]

    def get(self, request):
        my_friends = FriendRequest.objects.get(friend_user=request.user, my_user=request.user)
        serializer = FriendsViewSerializer(data=request.user)
        return Response(serializer(my_friends).data)

