from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    pic = models.URLField(default='https://i.imgur.com/EqUd38p.png', max_length=200)
    bio = models.TextField(blank = True, max_length=500)

    def __str__(self):
        return self.username


# class Profile(models.Model):
#     user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

#     bio = models.TextField(blank = True, max_length=500)

#     pic = models.URLField(default='https://i.imgur.com/EqUd38p.png', max_length=200)

    
#     #pic = models.ImageField(default='default.jpg', upload_to='profile_pics')

#     def __str__(self):
#         return f'{self.user.username} Profile'

#     # def save(self):
#     #     super().save()

#     #     img = Image.open(self.image.path)

#     #     if img.height > 300 or img.width > 300:
#     #         output_size = (300,300)
#     #         img.thumbnail(output_size)
#     #         img.save(self.image.path)