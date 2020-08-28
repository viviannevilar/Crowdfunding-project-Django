from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<str:username>/', views.UserRetrieveUpdateDestroy.as_view()),
    path('register/', views.UserCreate.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
