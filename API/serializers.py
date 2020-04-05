from rest_framework import serializers
from main.models import User, Hero, Photo, Comment, Post


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
        instance.name = validated_data.get('name', instance.name)
        instance.surname = validated_data.get('surname', instance.surname)
        instance.stage = validated_data.get('stage', instance.stage)
        instance.karma = validated_data.get('karma', instance.karma)
        instance.urlVK = validated_data.get('urlVK', instance.urlVK)
        instance.save()
        return instance


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
        instance.name = validated_data.get('name', instance.name)
        instance.surname = validated_data.get('surname', instance.surname)
        instance.father_name = validated_data.get('father_name', instance.father_name)
        instance.info = validated_data.get('info', instance.info)
        instance.bd = validated_data.get('bd', instance.bd)
        instance.dd = validated_data.get('dd', instance.dd)
        instance.army_name = validated_data.army_name('army_name', instance.army_name)
        instance.army_name_short = validated_data.get('army_name_short', instance.army_name_short)
        instance.save()
        return instance


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
        return Photo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update current `Photo` instance
        :param instance: existing `Photo` instance
        :param validated_data: request data
        :return: updated `Photo` instance
        """
        instance.img = validated_data.get('img', instance.img)
        instance.year = validated_data.get('year', instance.year)
        instance.isAvatar = validated_data.get('isAvatar', instance.isAvatar)
        instance.save()
        return instance

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
        return Photo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update current `Photo` instance
        :param instance: existing `Photo` instance
        :param validated_data: request data
        :return: updated `Photo` instance
        """
        instance.img = validated_data.get('img', instance.img)
        instance.year = validated_data.get('year', instance.year)
        instance.isAvatar = validated_data.get('isAvatar', instance.isAvatar)
        instance.save()
        return instance



class PostDetailSerializer(serializers.ModelSerializer):
    """
    Serializer for Post and information about it
    """
    class Meta:
        model = Post
        fields = '__all__'

    def create(self, validated_data):
        """
        Create a new `Post` instance
        :param validated_data: request data
        :return: new `Post` instance
        """
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update current `Post` instance
        :param instance: existing `Post` instance
        :param validated_data: request data
        :return: updated `Post` instance
        """
        instance.like = validated_data.get('like', instance.like)
        instance.save()
        return instance


class CommentDetailSerializer(serializers.ModelSerializer):
    """
    Serializer for Post and information about it
    """
    class Meta:
        model = Comment
        fields = '__all__'

    def create(self, validated_data):
        """
        Create a new `Comment` instance
        :param validated_data: request data
        :return: new `Comment` instance
        """
        return Comment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update current `Comment` instance
        :param instance: existing `Comment` instance
        :param validated_data: request data
        :return: updated `Comment` instance
        """
        instance.text = validated_data.get('text', instance.text)
        instance.save()
        return instance
