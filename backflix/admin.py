from django.contrib import admin
from backflix.models import Video, Categoria


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'cor')
    list_display_links = ('id', 'titulo')
    search_fields = ('titulo',)
    list_per_page = 10


class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'descricao', 'url', 'categoria')
    list_display_links = ('id', 'titulo')
    search_fields = ('titulo', 'descricao')
    list_per_page = 10
    ordering = ('titulo',)


admin.site.register(Video, VideoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
