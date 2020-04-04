from django.db import models

STATUS = (
    (1, "STATUS_DEFAULT"),
    (2, "STATUS_REQUESTED"),
    (3, "STATUS_APPROVED"),
)


# Create your models here.
class User(models.Model):
    """
    User object
    """
    name = models.CharField(max_length=200, unique=False)
    surname = models.CharField(max_length=200, unique=False)
    stage = models.IntegerField(default=0)
    urlVK = models.CharField(max_length=100, blank=True)


class Hero(models.Model):
    """
    Object of Great War Member
    """
    name = models.CharField(max_length=200, unique=False)
    surname = models.CharField(max_length=200, unique=False)
    member = models.ForeignKey(User, on_delete=models.CASCADE)


class Photo(models.Model):
    """
    Object of heroes photo
    """
    img = models.ImageField()
    year = models.IntegerField()
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE)

