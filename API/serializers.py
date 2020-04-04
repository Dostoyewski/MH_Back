from rest_framework import serializers
from main.models import User, Hero, Photo

class UserDetailSerializer(serializers.ModelSerializer):
    """Serilizer for users (who will post)"""
    class Meta:
        model = User
        fields = '__all__'


class HeroDetailSerializer(serializers.ModelSerializer):
    """Serilizer for information about Great War Members"""
    class Meta:
        model = Hero
        fields = '__all__'


class PhotoDetailSerializer(serializers.ModelSerializer):
    """Serilizer for iphotos and nformation about it"""
    class Meta:
        model = Photo
        fields = '__all__'       


