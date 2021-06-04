from django.db import models

class CarItemManager(models.Manager):
    
    def add_item(self,chave,produto):
        #A chave é referente a chave da sessão
        if self.filter(chave=chave,produto=produto).exists():
            created =False
            carItem = self.get(chave=chave,produto=produto)
        else:
            created=True
            carItem = CarItem.objects.create(chave=chave,produto=produto,preco=produto.preco)
        
        if not created:
            carItem.quantidade+=1                         
            carItem.save()
            
        return carItem,created

class CarItem(models.Model):
    chave = models.CharField('Chave do Carrinho',max_length=40,db_index=True)
    produto = models.ForeignKey('catalogo.Produto',verbose_name='Produto',on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField('Quantidade',default=1)
    preco = models.DecimalField('Preço',decimal_places=2,max_digits=8)
    
    objects = CarItemManager()
    
    class Meta:
        verbose_name ="Item do Carrinho"
        verbose_name_plural = "Itens dos carrinhos"
        unique_together = (('chave','produto'),)
    
    def __str__(self):
        return "{0} [{1}]".format(self.produto,self.quantidade)
    
    