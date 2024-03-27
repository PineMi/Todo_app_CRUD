from rest_framework.serializers import ModelSerializer, Serializer
from .models import User, Profile


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email", "password")
        extra_kwargs = {'password': {'write_only': True, 'min_length': 8}}


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ('name',)


class RegisterSerializer(Serializer):
    profile = ProfileSerializer()
    user = UserSerializer()

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        profile_data = validated_data.pop("profile")

        user = User.objects.create_user(**user_data)
        profile = Profile.objects.create(user=user,**profile_data)
        return user
    
