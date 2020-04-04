from rest_framework import serializers
from .models import User, Hero, Photo


class UserSerializer(serializers.Serializer):
    """
    Serializer for user model
    """
    id = serializers.IntegerField(read_only=True)
    stage = serializers.IntegerField(default=0)
    exp = serializers.IntegerField(default=0)
    name = serializers.CharField(max_length=200)
    surname = serializers.CharField(max_length=200)
    urlVK = serializers.CharField(max_length=200)

    def create(self, validated_data):
        """
        Create and return a new `User` instance, given the validated data.
        :param validated_data: checked data
        :return: new `User` instance
        """
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `User` instance, given the validated data.
        This function updates only stage and experience.
        :param instance: existing `User` instance
        :param validated_data: validated data
        :return: updated `User` instance
        """
        instance.stage = validated_data.get('stage', instance.stage)
        instance.exp = validated_data.get('exp', instance.exp)
        instance.save()
        return instance

        
class HeroSerializer(serializers.Serializer):
    """

    """
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(default='Не задано')
    surname = serializers.CharField(default='Не задано')
    father_name = serializers.CharField(default='Не задано')
    info = serializers.CharField(default='Не задано')
    army_name = serializers.CharField(default='Не задано')
    army_name_short = serializers.CharField(default='Не задано')

    def create(self, validated_data):
        """
        Create and return a new `Hero` instance, given the validated data.
        :param validated_data: checked data
        :return: new `Hero` instance
        """
        return Hero.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Hero` instance, given the validated data.
        This function updates all hero params
        :param instance: existing `Hero` instance
        :param validated_data: validated data
        :return: updated `Hero` instance
        """
        instance.name = validated_data.get('name', instance.name)
        instance.surname = validated_data.get('surname', instance.surname)
        instance.father_name = validated_data.get('father_name', instance.father_name)
        instance.info = validated_data.get('info', instance.info)
        instance.army_name = validated_data.get('army_name', instance.army_name)
        instance.army_name_short = validated_data.get('army_name_short', instance.army_name_short)
        instance.save()
        return instance


class PhotoSerializer(serializers.Serializer):
    """

    """
    id = serializers.IntegerField(read_only=True)
    year = serializers.IntegerField()
    img = serializers.ImageField()

    def create(self, validated_data):
        """
        Create and return a new `Photo` instance, given the validated data.
        :param validated_data: checked data
        :return: new `Photo` instance
        """
        return Photo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Photo` instance, given the validated data.
        This function updates only stage and experience.
        :param instance: existing `Photo` instance
        :param validated_data: validated data
        :return: updated `Photo` instance
        """
        instance.year = validated_data.get('year', instance.year)
        instance.save()
        return instance

