from django.conf import settings
from django.db import models
from django.db.models import SET_NULL
import random


class Post(models.Model):
    content = models.TextField(
        verbose_name='content'
    )
    user = models.ForeignKey(
        verbose_name='user',
        to=settings.AUTH_USER_MODEL,
        on_delete=SET_NULL,
        related_name='posts',
        null=True,
    )

    created = models.DateTimeField(
        verbose_name='created',
        auto_now_add=True
    )

    share_relation = models.TextField(
        verbose_name='share_relation',
        null=True,
    )

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.content


class Like(models.Model):
    user = models.ForeignKey(
        verbose_name='user',
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    post = models.ForeignKey(
        verbose_name='post',
        to='feed.Post',
        on_delete=models.CASCADE,
        related_name='likes'
    )

    class Meta:
        unique_together = [
            ('user', 'post'),
        ]

    def __str__(self):
        return f"{self.user}_{self.post}"


def code_generator():
    return random.randint(1000, 9999)


class UserProfile(models.Model):
    user = models.OneToOneField(
        verbose_name='user',
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="user_profile",
    )

    followees = models.ManyToManyField(
        verbose_name='following',
        to=settings.AUTH_USER_MODEL,
        related_name='followers',
    )

    registration_code = models.CharField(
        verbose_name='registration_code',
        max_length=15,
        unique=True,
        default=code_generator
    )
    friends = models.ManyToManyField(
        verbose_name='friends',
        to=settings.AUTH_USER_MODEL,
        related_name='friends',
    )

    sprichwort = models.CharField(
        verbose_name='sprichwort',
        max_length=150,
        null=True,
    )

    def __str__(self):
        return f"User: {self.user}\nFollowees: {self.followees}\n Sprichwort: {self.sprichwort}"


class FriendRequest(models.Model):

    my_user = models.ForeignKey(
        verbose_name='my_user',
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    friend_user = models.ForeignKey(
        verbose_name='friend_user',
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='friend_user'
    )
    DEFAULT_STATUS = "ACCEPTED"
    STATUS_CHOICES = [
        (DEFAULT_STATUS, "accepted"),
        ("PENDING", "pending"),
        ("DECLINED", "declined"),
    ]
    STATUS = models.CharField(
        max_length=200,
        choices=STATUS_CHOICES,
        default=DEFAULT_STATUS,
    )

    class Meta:
        unique_together = [
            ('my_user', 'friend_user'),
        ]

    def __str__(self):
        return f"{self.my_user}_{self.friend_user}"
