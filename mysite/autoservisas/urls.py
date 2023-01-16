from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('modeliai/', views.modeliai, name='modeliai'),
    path('automobiliai/', views.automobiliai, name='automobiliai')
]