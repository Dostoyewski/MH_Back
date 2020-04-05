from django.urls import path
from API.views import *


app_name = 'API'
urlpatterns = [
    path('user/create/', UserCreateView.as_view()),
    path('user/getlist/', UserListView.as_view()),
    path('user/detail/<int:pk>', user_detail),
    path('user/get_heroes/<int:pk>', get_heroes),
    path('hero/create/', HeroCreateView.as_view()),
    path('hero/getlist/', HeroListView.as_view()),
    path('hero/detail/<int:pk>', hero_detail),
    path('photo/create/', PhotoCreateView.as_view()),
    path('photo/getlist/', PhotoListView.as_view()),
    path('photo/detail/<int:pk>', photo_detail),
    path('Post/create/', PostCreateView.as_view()),
    path('Post/getlist/', PostListView.as_view()),
    path('Post/detail/<int:pk>', post_detail),
    path('Comment/create/', CommentCreateView.as_view()),
    path('Comment/getlist/', CommentListView.as_view()),
    path('Comment/detail/<int:pk>', comment_detail),


]
