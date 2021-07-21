from rest_framework import viewsets
from backflix.models import Video
from backflix.serializer import VideoSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class VideoViewSet(viewsets.ModelViewSet):
    """Exibindo todos os vídeos"""
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
