from rest_framework import serializers
from .models import User, Hero, Photo


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    stage = serializers.IntegerField(default=0)
    exp = serializers.CharField(default=0)

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
