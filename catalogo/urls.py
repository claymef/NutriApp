from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_alimentos, name='lista_alimentos'),
]