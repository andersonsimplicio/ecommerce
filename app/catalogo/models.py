from django.db import models
from django.urls import reverse

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField('Nome',max_length=120)
    slug = models.SlugField('Identificador', max_length=100)
    criado = models.DateTimeField('Criado em',auto_now_add=True)
    modificado = models.DateTimeField('Modificado em',auto_now=True)
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['nome']
    def __str__(self):
        return self.nome
    
    def get_absolute_url(self):
        return reverse("catalogo:lista_categoria", kwargs={"slug": self.slug})
    

class Produto(models.Model):
    nome = models.CharField('Nome',max_length=120)
    slug = models.SlugField('Identificador', max_length=100)
    criado = models.DateTimeField('Criado em',auto_now_add=True)
    modificado = models.DateTimeField('Modificado em',auto_now=True)
    categoria = models.ForeignKey("catalogo.Categoria", verbose_name="categoria", on_delete=models.CASCADE)
    descricao = models.TextField('Descrição',blank=True)
    preco = models.DecimalField('Preço',decimal_places=2,max_digits=10)
    
    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['nome']
        
    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("catalogo:produto_details", kwargs={"slug": self.slug})