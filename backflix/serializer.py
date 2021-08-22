from rest_framework import serializers
from backflix.models import Video, Categoria
import validators


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'
        extra_kwargs = {
            'titulo': {
                'error_messages': {'blank': 'O campo é obrigatório', 'null': 'O campo é obrigatório'}
            },
            'cor': {
                'error_messages': {'blank': 'O campo é obrigatório', 'null': 'O campo é obrigatório'}
            }
        }

    def validate_cor(self, cor):
        if len(cor) < 7:
            raise serializers.ValidationError("A cor deve ter exatamente 7 caracteres. Exemplo: '#FA1234'")
        if cor[0] != '#':
            raise serializers.ValidationError('O primeiro caractere da cor deve ser #')
        for c in cor[1:]:
            if not c.isnumeric() and c not in ['A', 'B', 'C', 'D', 'E', 'F']:
                raise serializers.ValidationError("A cor deve estar no padrão RGB. Exemplo: '#AB1234'")
        return cor


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'

    def validate_url(self, url):
        if not validators.url(url):
            raise serializers.ValidationError('URL inválida')
        return url


class VideosPorCategoriaSerializer(serializers.ModelSerializer):
    titulo = serializers.ReadOnlyField()
    url = serializers.ReadOnlyField()
    descricao = serializers.ReadOnlyField()

    class Meta:
        model = Video
        fields = ['titulo', 'url', 'descricao']
