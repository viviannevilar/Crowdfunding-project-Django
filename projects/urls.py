from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views



urlpatterns = [
    path('projects/', views.ProjectList.as_view()),
    path('project/<int:pk>/', views.ProjectDetail.as_view()),
    path('myprojects/', views.OwnerProjectList.as_view()),
    path('pledges/', views.PledgeList.as_view()),
    path('categories/', views.CategoryList.as_view()),
    path('categories/<str:name>/', views.CategoryDetail.as_view()),
    path('favourites/', views.FavouriteListView.as_view()),
    path('project/<int:pk>/favourite/', views.FavouriteView.as_view()),
    path('project/<int:pk>/publish', views.ProjectPublish.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)