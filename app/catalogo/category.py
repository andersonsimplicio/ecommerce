from .models import Categoria

def categorias(request):
    categorias = Categoria.objects.all()
    return {'categorias':categorias}