from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils.timezone import now
from datetime import datetime, timedelta

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
    date_created = models.DateTimeField(auto_now_add=True) 
    duration = models.IntegerField()
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
    favouriters = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='favouriter_projects',
        through='Favourite'
        )

    @property
    def is_open(self):
        if self.pub_date is None:
            return False
        return (self.pub_date + timedelta(self.duration)) > now()

# Check ben's suggestion to override the save method on the model to close it after a certain amount is reached.
    # You can override the save method on your model to check and update the field before saving.
    # def save(self, *args, **kwargs):
    #     if self.pledge >= self.target
    #     self.complete=True
    #     return super().save(*args, **kwargs)

    #https://www.django-rest-framework.org/api-guide/fields/#serializermethodfield


class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    date_sent = models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
        related_name='project_pledges'
    )
    supporter = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
        related_name = 'supporter_pledges'
    )

class Favourite(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
        related_name = 'owner_favourites',
    )
    project = models.ForeignKey(
        Project,
        on_delete = models.CASCADE,
        related_name = 'projects_favourites'
    )
    date = models.DateTimeField(auto_now_add=True)