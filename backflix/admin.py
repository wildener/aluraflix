from django.contrib import admin
from backflix.models import Video


class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'descricao', 'url')
    list_display_links = ('id', 'titulo')
    search_fields = ('titulo',)
    list_per_page = 20


admin.site.register(Video, VideoAdmin)
