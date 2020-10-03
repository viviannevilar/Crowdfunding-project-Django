from django.contrib import admin
from .models import Project, Category, Pledge, Favourite


class ProjectAdmin(admin.ModelAdmin):
    model = Project
    list_display = ['title','id','owner', 'is_open']


admin.site.register(Project,ProjectAdmin)
admin.site.register(Category)
admin.site.register(Pledge)
admin.site.register(Favourite)