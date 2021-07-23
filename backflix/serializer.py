from rest_framework import serializers
from backflix.models import Video
import validators


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'titulo', 'descricao', 'url']

    def validate_url(self, url):
        if not validators.url(url):
            raise serializers.ValidationError('URL inválida')
        return url
