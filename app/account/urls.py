from django.urls import path
from .views import RegisterView

urlpatterns = [
    path('registro/',RegisterView.as_view(),name='registro'),
]