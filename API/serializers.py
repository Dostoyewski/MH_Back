from rest_framework import serializers
from main.models import User, Hero, Photo


class UserDetailSerializer(serializers.ModelSerializer):
    """
    Serializer for users (who will post)
    """
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        """
        Create a new `User` instance
        :param validated_data: request data
        :return: new `User` instance
        """
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update current `User` instance
        :param instance: existing `User` instance
        :param validated_data: request data
        :return: updated `User` instance
        """
        # TODO: Write fields setters


class HeroDetailSerializer(serializers.ModelSerializer):
    """
    Serializer for information about Great War Members
    """
    class Meta:
        model = Hero
        fields = '__all__'

    def create(self, validated_data):
        """
        Create a new `Hero` instance
        :param validated_data: request data
        :return: new `Hero` instance
        """
        return Hero.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update current `Hero` instance
        :param instance: existing `Hero` instance
        :param validated_data: request data
        :return: updated `Hero` instance
        """
        # TODO: Write fields setters


class PhotoDetailSerializer(serializers.ModelSerializer):
    """
    Serializer for photos and information about it
    """
    class Meta:
        model = Photo
        fields = '__all__'

    def create(self, validated_data):
        """
        Create a new `Photo` instance
        :param validated_data: request data
        :return: new `Photo` instance
        """
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update current `Photo` instance
        :param instance: existing `Photo` instance
        :param validated_data: request data
        :return: updated `Photo` instance
        """
        # TODO: Write fields setters
