from django.shortcuts import render
from rest_framework import generics
from API.serializers import UserDetailSerializer, HeroDetailSerializer, PhotoDetailSerializer
from main.models import User, Photo, Hero
from API.permissions import IsOwnerOrReadOnly


class UserCreateView(generics.CreateAPIView):
    """
    User creation view
    """
    serializer_class = UserDetailSerializer
    permission_classes = (IsOwnerOrReadOnly, )


class UserListView(generics.ListAPIView):
    """
    User list view
    """
    serializer_class = UserDetailSerializer
    queryset = User.objects.all()
    permission_classes = (IsOwnerOrReadOnly, )


class HeroCreateView(generics.CreateAPIView):
    """
    Hero creation view
    """
    serializer_class = HeroDetailSerializer
    permission_classes = (IsOwnerOrReadOnly, )


class HeroListView(generics.ListAPIView):
    """
    Hero list view
    """
    serializer_class = HeroDetailSerializer
    queryset = Hero.objects.all()
    permission_classes = (IsOwnerOrReadOnly, )


class PhotoCreateView(generics.CreateAPIView):
    """
    Photo creation view
    """
    serializer_class = PhotoDetailSerializer
    permission_classes = (IsOwnerOrReadOnly, )


class PhotoListView(generics.ListAPIView):
    """
    Photo list view
    """
    serializer_class = PhotoDetailSerializer
    queryset = Photo.objects.all()
    permission_classes = (IsOwnerOrReadOnly, )
