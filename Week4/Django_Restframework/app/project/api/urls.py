from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)
from project.api.views.main_views import FeedDisplayView, PostGetUpdateDeleteView, UserDisplayView, PostCreateView, \
    LikeView, FollowingView, DislikeView, SharePostView, UserProfileView, \
    FriendsDeleteView, FriendsRequestGeneralView, FriendsRequestMyView, FriendsRequestStatusAccept, \
    FriendsSimplePostView, FriendsRequestStatusReject
from project.api.views import registration
from project.api.views.registration import PasswordResetView, PasswordResetValidationView
from django.urls import path

app_name = 'api'


urlpatterns = [
    path('feed/', FeedDisplayView.as_view(), name='feed_display'),
    path('feed/<int:user_id>/', UserDisplayView.as_view(), name='feed_post_display'),
    path('feed/followers/', FollowingView.as_view(), name='feed_follower_display'),
    path('feed/?search=<str:search_string>', FeedDisplayView.as_view(), name='feed_search'),
    path('feed/friends/', FriendsSimplePostView.as_view(), name='feed_post_display'),# lists all of your friends
    path('posts/<int:post_id>/', PostGetUpdateDeleteView.as_view(), name='post_display'),
    path('posts/new-post/', PostCreateView.as_view(), name='New_Post'),
    path('posts/likes/', LikeView.as_view(), name='likePerPerson'),
    path('posts/like/<int:post_id>/', LikeView.as_view(), name='likePerPost'),
    path('posts/<int:post_id>/dislike/', DislikeView.as_view(), name='dislike_post'),
    path('posts/share-post/<int:post_id>', SharePostView.as_view(), name='share_post'),

    path('users/follow/<int:user_id>/', FollowingView.as_view(), name='followUser'),

    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh', TokenObtainPairView.as_view(), name='token_refresh'),
    path('auth/password-reset/', PasswordResetView.as_view(), name='password_resets'),
    path('auth/password-reset/validation/', PasswordResetValidationView.as_view(), name='password_reset_validation'),

    path('me/', UserProfileView.as_view(), name='user_profile'),

    path('users/friendrequests/', FriendsRequestGeneralView.as_view(), name='list_friends'),# get: lists all friend requests
    path('users/friendrequests/<int:user_id>/', FriendsRequestGeneralView.as_view(), name='send_friend_request'),# post: sends a friend request
    path('users/friendrequests/pending/', FriendsRequestMyView.as_view(), name='friendships_pending'),# get: lists all of MY pending friendrequests
    path('users/friendrequests/accept/<int:request_id>/', FriendsRequestStatusAccept.as_view(), name='friendship_accept'),# accepts a friendrequest
    path('users/friendrequests/accept/<int:request_id>/', FriendsRequestStatusReject.as_view(), name='friendship_accept'),# rejects a friendrequest
    path('users/friends/unfriend/', FriendsDeleteView.as_view(), name='friendship_delete'),# deletes friendship

    path('registration/', registration.RegistrationView.as_view(), name='registration'),
    path('registration/validation/', registration.RegistrationValidationView.as_view(), name='registration_validation'),
]
