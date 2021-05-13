from django.contrib import admin
from .models import Produto,Categoria

class ProdutoAdm(admin.ModelAdmin):
    list_display = ['nome','preco','criado','categoria']
    search_fields = ['nome','slug','categoria__nome']
    list_filter = ['criado','modificado']
class CategoriaAdm(admin.ModelAdmin):
    list_display = ['nome','criado']
    search_fields = ['nome','slug']

admin.site.register(Produto,ProdutoAdm)
admin.site.register(Categoria,CategoriaAdm)

