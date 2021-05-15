#config=utf-8
from django import forms
from django.shortcuts import render,get_list_or_404
from app.catalogo.models import Categoria,Produto
from .forms import ContactFrom
def index(request):
    template='core/index.html'
    context = {
        'title':'Amazon',
    }
    return render(request,template,context=context)

def contato(request):
    template='core/contact.html'
    
    if request.method == 'POST':
        form = ContactFrom(request.POST)
        
    else:
        form = ContactFrom()
        
    context = {
        'title':'Contato',
        'form':form
    }
    
    return render(request,template,context=context)


