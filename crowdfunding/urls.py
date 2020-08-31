from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('projects.urls')),
    path('users/', include('users.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('projects.urls')),
#     path('', include('users.urls')),
#     path('api-auth/', include('rest_framework.urls')),
#     path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
# ]
