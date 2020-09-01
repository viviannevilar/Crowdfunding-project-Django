from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    pic = models.URLField(default='https://i.imgur.com/EqUd38p.png', max_length=200)
    bio = models.TextField(blank = True, max_length=500)

    def __str__(self):
        return self.username
        


