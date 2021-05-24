#config=utf-8
from django import forms
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render,get_list_or_404, resolve_url
from app.catalogo.models import Categoria,Produto
from .forms import ContactFrom
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.views.generic import TemplateView

User = get_user_model()

class IndexView(TemplateView):
    template_name = 'core/index.html'
    
    def get_context_data(self, **kwargs):
        context = {
        'title':'Amazon',
        }
        return context


  
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


