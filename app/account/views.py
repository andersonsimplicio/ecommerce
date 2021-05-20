from django.http import request
from django.shortcuts import render
from django.views.generic import CreateView,TemplateView,UpdateView,FormView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User
from .forms import UserAdminCreationForm
from django.contrib.auth.forms import PasswordChangeForm

class IndexView(LoginRequiredMixin,TemplateView):
    template_name='account/index.html'

class RegisterView(CreateView):
    form_class = UserAdminCreationForm
    template_name = 'account/registro.html'
    model = User
    success_url =reverse_lazy('index')

class UpdateUserView(LoginRequiredMixin,UpdateView):
    model = User
    template_name = "account/update_user.html"
    fields = ['name','email']
    success_url =reverse_lazy('account:index')
    
    def get_object(self):
        return self.request.user


class PasswordView(LoginRequiredMixin,FormView):
    template_name = "account/update_password.html"
    form_class = PasswordChangeForm
    success_url =reverse_lazy('account:index')
    
    def get_form_kwargs(self):
        kwargs = super(PasswordView,self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs