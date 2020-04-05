from django.shortcuts import render
from rest_framework import generics
from API.serializers import UserDetailSerializer, HeroDetailSerializer, PhotoDetailSerializer, PostDetailSerializer, CommentDetailSerializer
from main.models import User, Photo, Hero, Comment, Post
from main.serializers import UserSerializer, HeroSerializer, PhotoSerializer, PostSerializer, CommentSerializer
from API.permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from get_path import get_path


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


class PostCreateView(generics.CreateAPIView):
    """
    Post creation view
    """
    serializer_class = PostDetailSerializer
    permission_classes = (IsOwnerOrReadOnly, )


class PostListView(generics.ListAPIView):
    """
    User list view
    """
    serializer_class = PostDetailSerializer
    queryset = Post.objects.all()
    permission_classes = (IsOwnerOrReadOnly, )


class CommentCreateView(generics.CreateAPIView):
    """
    Comment creation view
    """
    serializer_class = CommentDetailSerializer
    permission_classes = (IsOwnerOrReadOnly, )


class CommentListView(generics.ListAPIView):
    """
    Comment list view
    """
    serializer_class = CommentDetailSerializer
    queryset = Comment.objects.all()
    permission_classes = (IsOwnerOrReadOnly, )



@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
    """
    Retrieve, update or delete user
    You can only change fields 'exp' and 'stage'
    :param request: request
    :param pk: User's id in db
    :return: Response
    """
    try:
        snippet = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def hero_detail(request, pk):
    """
    Retrieve, update or delete hero
    :param request: request
    :param pk: Hero's id in db
    :return: Response
    """
    try:
        snippet = Hero.objects.get(pk=pk)
    except Hero.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = HeroSerializer(snippet)
        data = serializer.data
        data['photos'] = PhotoSerializer(Photo.objects.filter(hero__pk=pk, isAvatar=False), many=True).data
        data['avatar'] = PhotoSerializer(Photo.objects.filter(hero__pk=pk, isAvatar=True), many=True).data
        return Response(data)

    elif request.method == 'PUT':
        serializer = HeroSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def photo_detail(request, pk):
    """
    Retrieve, update or delete photo
    :param request: request
    :param pk: Photo's id in DB
    :return: Response
    """
    try:
        snippet = Photo.objects.get(pk=pk)
    except Photo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PhotoSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PhotoSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'PUT', 'DELETE'])
def post_detail(request, pk):
    """
    Retrieve, update or delete user
    You can only change fields 'like' 
    :param request: request
    :param pk: Post's id in db
    :return: Response
    """
    try:
        snippet = Post.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PostSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PostSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def comment_detail(request, pk):
    """
    Retrieve, update or delete user
    You can only change fields 'text' 
    :param request: request
    :param pk: Comment's id in db
    :return: Response
    """
    try:
        snippet = Post.objects.get(pk=pk)
    except Comment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CommentSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CommentSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def get_heroes(request, pk):
    """
    This function return all User's heroes
    :param request: request data
    :param pk: User's VK id
    :return: JSON with heroes
    """
    try:
        snippet = Hero.objects.filter(member__urlVK=pk)
    except Hero.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        response = []
        for obj in snippet:
            serializer = HeroSerializer(obj)
            data = serializer.data
            data['photos'] = PhotoSerializer(Photo.objects.filter(hero__pk=obj.pk, isAvatar=False), many=True).data
            try:
                data['avatar'] = PhotoSerializer(Photo.objects.filter(hero__pk=obj.pk, isAvatar=True), many=True).data[0]['img']
            except IndexError:
                data['avatar'] = None
            response.append(data)
        return Response(response)


@api_view(['GET'])
def get_path_pk(request, pk):
    """
    This function returns army path
    :param request: request
    :param pk: object id
    :return: path
    """
    info = Hero.objects.get(pk=pk).army_name
    try:
        return Response(get_path(info))
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_path_str(request, info):
    """
    This function returns army unit path
    :param request: request
    :param info: army unit name
    :return: JSON with path
    """
    try:
        return Response(get_path(info))
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def update_all_path(request):
    """
    This function will update path field for all heroes
    :param request: request
    :return: 200 if OK, 503 if FAIL
    """
    heroes = Hero.objects.all()
    try:
        for hero in heroes:
            hero.path = get_path(hero.army_name)
            hero.save(force_update=True)
        return Response(status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_503_SERVICE_UNAVAILABLE)
