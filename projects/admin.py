from django.contrib import admin
from .models import Project, Category, Pledge, Favourite

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    model = Project
    list_display = ['title','id','owner', 'is_open']
    #fields = ('title', 'id', 'owner', 'favouriters')


class PledgeAdmin(admin.ModelAdmin):
    model = Pledge
    list_display = ['id','supporter', 'project', 'date_sent', 'project_owner']

#admin.site.register(Project,ProjectAdmin)
admin.site.register(Category)
admin.site.register(Pledge,PledgeAdmin)
admin.site.register(Favourite)


