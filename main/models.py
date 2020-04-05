from django.db import models

GRADE = (
    (0, "Рядовой"),
    (1, "Прапорщик"),
    (2, "Лейтенант"),
    (3, "Майор"),
    (4, "Полковник"),
    (5, "Генерал"),
)


# Create your models here.
class User(models.Model):
    """
    User object
    """
    name = models.CharField(max_length=200, unique=False)
    surname = models.CharField(max_length=200, unique=False)
    stage = models.IntegerField(choices=GRADE, default=0)
    exp = models.IntegerField(default=0)
    urlVK = models.CharField(max_length=100, blank=True, unique=True)


class Hero(models.Model):
    """
    Object of Great War Member
    """
    name = models.CharField(max_length=200, unique=False)
    surname = models.CharField(max_length=200, unique=False)
    father_name = models.CharField(max_length=200, unique=False, blank=True)
    # Short info about Ded
    info = models.TextField(max_length=1000, unique=False, default="Нет информации")
    member = models.ForeignKey(User, on_delete=models.CASCADE)
    stage = models.CharField(max_length=100, default=0)
    # Ded's birth date
    bd = models.DateField(null=True, blank=True)
    # Ded's death date
    dd = models.DateField(null=True, blank=True)
    # Military unit name
    army_name = models.CharField(max_length=50, blank=True, unique=False)
    # Military unit short name
    army_name_short = models.CharField(max_length=10, blank=True, unique=False)
    # Path of Ded's military unit
    path = models.TextField(max_length=1000, blank=True, unique=False)


class Photo(models.Model):
    """
    Object of heroes photo
    """
    img = models.ImageField()
    year = models.IntegerField()
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE)
    # Hero's profile avatar flag
    isAvatar = models.BooleanField(default=False)


class Post(models.Model):
    """
    Post model
    """
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE)
    like = models.IntegerField()


class Comment(models.Model):
    """
    Comment post
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)