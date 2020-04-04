from django.urls import path
from API.views import *


app_name = 'API'
urlpatterns = [
    path('user/create/', UserCreateView.as_view()),
    path('user/getlist/', UserListView.as_view()),
    path('hero/create/', HeroCreateView.as_view()),
    path('hero/getlist/', HeroListView.as_view()),
    path('photo/create/', PhotoCreateView.as_view()),
    path('photo/getlist/', PhotoListView.as_view()),
]
