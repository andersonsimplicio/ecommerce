from django.urls import path
from .views import RegisterView,IndexView,UpdateUserView,PasswordView

urlpatterns = [
    path('',IndexView.as_view(),name='index'),
    path('registro/',RegisterView.as_view(),name='registro'),
    path('alterar-dados/',UpdateUserView.as_view(),name='alterarDados'),
    path('alterar-senha/',PasswordView.as_view(),name='update_password'),
]