from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.ProjectList.as_view()),
    path('<int:pk>/', views.ProjectDetail.as_view()),
    path('pledges/', views.PledgeList.as_view()),
    path('categories/', views.CategoryList.as_view()),
    path('categories/<str:name>/', views.CategoryDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)