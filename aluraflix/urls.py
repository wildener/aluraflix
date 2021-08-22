"""aluraflix URL Configuration"""
from django.contrib import admin
from django.urls import path, include
from backflix.views import VideoViewSet, CategoriaViewSet, VideosPorCategoriaListView, VideosSemAutenticacaoListView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('videos', VideoViewSet, basename='Videos')
router.register('categorias', CategoriaViewSet, basename='Categorias')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('categorias/<int:categoria_id>/videos/', VideosPorCategoriaListView.as_view()),
    path('videos/free', VideosSemAutenticacaoListView.as_view()),
]
