from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.UserList.as_view()),
    path('register/', views.UserCreate.as_view()),    
    path('<str:username>/', views.UserRetrieveUpdateDestroy.as_view()),
    #path('<str:username>/profile/',views.UserProfile.as_view()),
    path('<int:pk>/profile/',views.UserProfile.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
