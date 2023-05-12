from django.contrib import admin
from videos.models import Video, Categoria


class Videos(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'descricao', 'url', 'categoria')
    list_display_links = ('id', 'titulo')
    search_fields = ('titulo',)
    list_per_page = 20


admin.site.register(Video, Videos)

class Categorias(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'cor')
    list_display_links = ('id', 'titulo')
    search_fields = ('titulo',)
    list_per_page = 20


admin.site.register(Categoria, Categorias)