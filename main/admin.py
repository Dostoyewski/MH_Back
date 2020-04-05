from django.contrib import admin
from .models import User, Hero, Photo, Post, Comment


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'exp', 'stage', 'urlVK')
    search_fields = ['name', 'surname', 'stage', 'urlVK']


class HeroAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'father_name', 'stage', 'bd', 'dd', 'army_name', 'member')
    search_fields = ['name', 'surname', 'father_name', 'stage', 'bd', 'dd', 'army_name', 'member']


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('img', 'year', 'hero', 'isAvatar')
    search_fields = ['img', 'year', 'hero', 'isAvatar']


class PostAdmin(admin.ModelAdmin):
    list_display = ('hero', 'like')
    search_fields = ['hero', 'like']


class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'text')
    search_fields = ['post', 'user', 'text']


admin.site.register(User, UserAdmin)
admin.site.register(Hero, HeroAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)