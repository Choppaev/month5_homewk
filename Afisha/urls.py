"""
URL configuration for Afisha project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from movie_app.views import *

list_create = {
    'get': 'list',
    'post': 'create'
}

update_retrieve_destroy = {
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('directors/', DirectorModelViewSet.as_view(list_create), name='directors-list'),
    path('directors/<int:pk>/', DirectorModelViewSet.as_view(update_retrieve_destroy), name='directors-detail'),
    path('movies/', MovieModelViewSet.as_view(list_create), name='movies-list'),
    path('movies/<int:pk>/', MovieModelViewSet.as_view(update_retrieve_destroy), name='movies-detail'),
    path('reviews/', ReviewModelViewSet.as_view(list_create), name='reviews-list'),
    path('reviews/<int:pk>/', ReviewModelViewSet.as_view(update_retrieve_destroy), name='reviews-detail'),
    path('movies/reviews/', ReviewMovieListAPIView.as_view(), name='movies-reviews'),
    path('api/v1/', include('users.urls'))
]

