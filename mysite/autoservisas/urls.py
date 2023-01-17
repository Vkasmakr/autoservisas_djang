from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('modeliai/', views.modeliai, name='modeliai'),
    path('automobiliai/', views.automobiliai, name='automobiliai'),
    path('automobiliai/<int:auto_id>', views.automobile, name='auto-detail'),
    path('uzsakymaseil/', views.OrdersListView.as_view(), name='uzsakymaseil'),
    path('uzsakymaseil/<int:ue_id>', views.orders_order, name='uzsakeil-detail')
]