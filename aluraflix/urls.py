"""aluraflix URL Configuration"""
from django.contrib import admin
from django.urls import path, include
from backflix.views import VideoViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('videos', VideoViewSet, basename='Videos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
