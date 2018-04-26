from django.contrib.auth import get_user_model
from django.core.mail import EmailMessage
from rest_framework import serializers
from project.feed.models import Post, Like, UserProfile, FriendRequest

User = get_user_model()


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(
        label='id'
    )
    username = serializers.CharField(
        label='username',
    )

    class Meta:
        model = User
        fields = ['id', 'first_name', 'username', 'post_count', 'fame_index']

class FriendRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['my_user', 'friend_user', 'STATUS_CHOICES']
        read_only_fields = ['created']

    def create (self, validated_data):
        return FriendRequest.object.create(
            my_user=self.context.get('my_user').user,
            friend_user=validated_data.get('friend_user'),
            STATUS='PENDING'
        )

class PostSerializer(serializers.ModelSerializer):
    like_count = serializers.IntegerField(
        read_only=True
    )

    class Meta:
        model = Post
        fields = ['id', 'content', 'created']
        read_only_fields = ['created']

    def create(self, validated_data):
        return Post.objects.create(
            content=validated_data.get('content'),
            user=self.context.get('request').user,
        )

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return {
            **data,
            'like_count': instance.likes.count()
        }


class FeedDisplaySerializer(PostSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'content', 'created', 'user']
        read_only_fields = ['id', 'created', 'user']


class LikeDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('user_id', 'post_id')
        read_only_fields = ['user_id', 'post_id']

    #    def count_likes(self, request):
    #        user = request.user

    def create(self, post):
        return Like.objects.create(
            user_id=self.context.get('request').user_id,
            post_id=post.post_id
        )


class followerDisplaySeriliazer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['user', 'followers']
        read_only_fields = ['user', 'followers']

    def showFollowers(self, user):
        return UserProfile.followees.count()


class ListPostsChronoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'content', 'created']
        read_only_fields = ['created']

    def get(self):
        return [p for p in Post]


class UserProfileDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['user', 'followees']
        read_only_fields = ['user', 'followees']


class SharePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['user', 'post', 'share_relation']
        read_only_fields = ['user', 'post', 'share_relation']


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['user', 'followees', 'sprichwort']
        read_only_fields = ['user', 'followees']


class RegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField(
        label='Email address'
    )

    def validate_email(self, value):
        try:
            User.objects.get(email=value)
        except User.DoesNotExist:
            return value

    def send_registration_email(self, email, code):
        message = EmailMessage(
            subject='Social feed registration',
            body=f"This is your registration code: {code}",
            to=[email],

        )
        message.send()

    def register_user(self, email):
        new_user = User.objects.create_user(
            username=email,
            email=email,
            is_active=False,
        )
        user_profile = UserProfile.objects.create(
            user=new_user,
        )
        self.send_registration_email(
            email=email,
            code=user_profile.registration_code,
        )
        return new_user


class RegistrationValidationSerializer(serializers.Serializer):
    code = serializers.CharField(
        label='validation_code',
        write_only=True
    )
    password = serializers.CharField(
        label='password',
        write_only=True,
    )
    password_repeat = serializers.CharField(
        label='password_repeat',
        write_only=True,
    )
    first_name = serializers.CharField(
        label='first_name'
    )
    last_name = serializers.CharField(
        label='last_name',
    )

    def validate(self, data):
        if data.get('password') != data.get('password_repeat'):
            raise serializers.ValidationError({
                'password': 'Passwords are not equal!'
            })
        return data

    def validate_code(self, value):
        try:
            return User.objects.get(
                user_profile__registration_code=value,
                is_active=False,
            )
        except User.DoesNotExist:
            raise serializers.ValidationError(
                'Wrong validation code!'
            )

    def save(self, validated_data):
        user = validated_data.get('code')
        user.first_name = validated_data.get('first_name')
        user.last_name = validated_data.get('last_name')
        user.is_active = True
        user.set_password(validated_data.get('password'))
        user.save()
        return user


class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField(
        label='Email address'
    )

    def validate_email(self, value):
        try:
            return User.objects.get(email=value)
        except User.DoesNotExist:
            raise serializers.ValidationError('User does not exist!')

    def pwReset_email(self, email, code):
        message = EmailMessage(
            subject='Password reset',
            body=f"This is your reset code: {code}",
            to=[email],
        )
        message.send()

    def send_pwReset_email(self, user):
        self.pwReset_email(
            email=user.email,
            code=user.user_profile.registration_code
        )
        return user

    def register_user(self, email):
        new_user = User.objects.create_user(
            username=email,
            email=email,
            is_active=False,
        )
        user_profile = UserProfile.objects.create(
            user=new_user,
        )
        self.send_registration_email(
            email=email,
            code=user_profile.registration_code,
        )
        return new_user


class PasswordResetValidationSerializer(serializers.Serializer):
    password = serializers.CharField(
        label='password',
        write_only=True,
    )
    password_repeat = serializers.CharField(
        label='password_repeat',
        write_only=True,
    )
    code = serializers.CharField(
        label='validation_code',
        write_only=True
    )

    def validate(self, data):
        if data.get('password') != data.get('password_repeat'):
            raise serializers.ValidationError({
                'password': 'Passwords are not equal!'
            })
        return data

    def validate_code(self, value):
        try:
            return User.objects.get(
                user_profile__registration_code=value,
            )
        except User.DoesNotExist:
            raise serializers.ValidationError(
                'Wrong validation code!'
            )

    def save(self, validated_data):
        user = validated_data.get('code')
        user.set_password(validated_data.get('password'))
        user.save()
        return 'Password reset!'


class FriendsViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendRequest
        fields = ['my_user', 'friend_user', 'STATUS']
        read_only_fields = fields

    def save(self, validated_data):
        friend_request = validated_data.get('STATUS')
        friend_request.save()
        return 'Password reset!'


'''
class FriendSerializer(serializers.Serializer):
    email = serializers.EmailField(
        label='Email address'
    )
    friend_email = serializers.EmailField(
        label='Friend Email address'
    )

    def validate_email(self, value):
        try:
            User.objects.get(email=value)

        except User.DoesNotExist:
            return value

    def send_registration_email(self, email, code):
        message = EmailMessage(
            subject='Social feed registration',
            body=f"This is your registration code: {code}",
            to=[email],

        )
        message.send()

'''
