from django.contrib import admin
from .models import Project, Category, Pledge, Favourite

# Register your models here.
admin.site.register(Project)
admin.site.register(Category)
admin.site.register(Pledge)
admin.site.register(Favourite)