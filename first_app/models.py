from django.db import models
from django.contrib.auth.models import User as authUser


# Create your models here.

class Topic(models.Model): 
    top_name = models.CharField(max_length=264, unique=True)

    def __str__(self): 
        return str(self.top_name)

class Webpage(models.Model): 
    topic = models.ForeignKey(Topic, models.SET_NULL, null=True)
    name = models.CharField(max_length=264, unique=True)
    url = models.URLField(unique=True)

    def __str__(self): 
        return str(self.name)

class AccessRecorder(models.Model): 
    name = models.ForeignKey(Webpage, models.SET_NULL, null=True)
    date = models.DateField()

    def __str__(self): 
        return str(self.date)

class User(models.Model): 
    first_name = models.CharField(max_length=264)
    last_name = models.CharField(max_length=264)
    email = models.EmailField(max_length=264)

    def __str__(self): 
        return str(self.first_name) + ' ' + str(self.last_name)


# Registration
class UserProfileInfo(models.Model): 
    # since class User is already been created, avoid collision with django.contrib.auth.models.User
    user = models.OneToOneField(authUser, on_delete=models.SET_NULL, null=True)
    profolio = models.URLField(blank=True)
    # file will be uploaded to MEDIA_ROOT
    picture = models.ImageField(upload_to='profile_imgs/')

    def __str__(self): 
        return str(self.user.username)