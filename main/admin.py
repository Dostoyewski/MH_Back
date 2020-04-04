from django.contrib import admin
from .models import User, Hero, Photo


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'exp', 'stage', 'urlVK')
    search_fields = ['name', 'surname', 'stage', 'urlVK']


class HeroAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'father_name', 'stage', 'bd', 'dd', 'army_name', 'member')
    search_fields = ['name', 'surname', 'father_name', 'stage', 'bd', 'dd', 'army_name', 'member']


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('img', 'year', 'hero')
    list_display = ['img', 'year', 'hero']


admin.site.register(User, UserAdmin)
admin.site.register(Hero, HeroAdmin)
admin.site.register(Photo, PhotoAdmin)