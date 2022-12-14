from rest_framework import serializers
from usuarios.models import User, UserProfile



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password']


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
    
