from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    profile = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self):
        return self.profile.username
