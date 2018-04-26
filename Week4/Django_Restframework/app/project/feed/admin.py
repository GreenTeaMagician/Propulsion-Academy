from django.contrib import admin

from project.feed.models import Post, Like, UserProfile, FriendRequest

admin.site.register(Post)
admin.site.register(Like)
admin.site.register(UserProfile)
admin.site.register(FriendRequest)
