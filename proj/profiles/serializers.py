from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'description', 'tags', 'username', 'email')
        extra_kwargs = {'tags': {'required': False}}

    username = serializers.CharField(source='user.username')
    email = serializers.EmailField(source='user.email')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create(**user_data)
        profile = Profile.objects.create(user=user, **validated_data)
        return profile

