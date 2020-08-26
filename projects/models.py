from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length = 15, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"

class Project(models.Model):
    title = models.CharField(max_length=200) 
    description = models.TextField()
    goal = models.IntegerField()
    image = models.URLField()
    is_open = models.BooleanField() 
    date_created = models.DateTimeField(auto_now_add=True) 
    pub_date =  models.DateTimeField(null=True,blank=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
        related_name = 'owner_projects',
    )
    category = models.ForeignKey(
        Category, 
        on_delete = models.SET_DEFAULT,
        default='Other',
        related_name = 'cat_projects'
    )

class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    date_sent = models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
        related_name='pledges'
    )
    supporter = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name = 'supporter_pledges'
    )