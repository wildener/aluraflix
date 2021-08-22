from rest_framework import viewsets, generics, filters
from backflix.models import Video, Categoria
from backflix.serializer import VideoSerializer, CategoriaSerializer, VideosPorCategoriaSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class VideoViewSet(viewsets.ModelViewSet):
    """Exibe todos os vídeos"""
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['titulo']
    search_fields = ['titulo']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class CategoriaViewSet(viewsets.ModelViewSet):
    """Exibe todas as categorias"""
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class VideosPorCategoriaListView(generics.ListAPIView):
    """Exibe os vídeos por categoria"""
    def get_queryset(self):
        queryset = Video.objects.filter(categoria_id=self.kwargs['categoria_id'])
        return queryset
    serializer_class = VideosPorCategoriaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class VideosSemAutenticacaoListView(generics.ListAPIView):
    """Exibe um número fixo de videos disponíveis, sem a necessidade de autenticação"""
    def get_queryset(self):
        num_videos = 10
        queryset = Video.objects.all().order_by('-id')[:num_videos]  # fixado em 10 vídeos
        return queryset
    serializer_class = VideosPorCategoriaSerializer
