from django.contrib import admin
from .models import Project, Category, Pledge, Favourite


class ProjectAdmin(admin.ModelAdmin):
    model = Project
    list_display = ['title','id','owner', 'is_open']

class PledgeAdmin(admin.ModelAdmin):
    model = Pledge
    list_display = ['id','supporter', 'date_sent']

admin.site.register(Project,ProjectAdmin)
admin.site.register(Category)
admin.site.register(Pledge,PledgeAdmin)
admin.site.register(Favourite)