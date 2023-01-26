from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('modeliai/', views.modeliai, name='modeliai'),
    path('automobiliai/', views.automobiliai, name='automobiliai'),
    path('automobiliai/<int:auto_id>', views.automobile, name='auto-detail'),
    path('uzsakymaseil/', views.OrdersListView.as_view(), name='uzsakymaseil'),
    path('uzsakymaseil/<int:pk>', views.OrderDetailView.as_view(), name='uzsakeil-detail'),
    path('search/', views.search, name='search'),
    path("accounts/", include("django.contrib.auth.urls")),
    path('myorders/', views.OrderDetailByUserListView.as_view(), name='my-orders'),
    path('register/', views.register, name='registration'),
    path('profilis/', views.profilis, name='profilis'),
    path('myorders/new', views.UzsakymoEiluteByUserCreateView.as_view(), name='my-order-new'),
    path('myorders/<int:pk>', views.UzsakymoEiluteByUserDetailView.as_view(), name='my-order'),
    path('myorders/<int:pk>/update', views.UzsakymoEiluteByUserUpdateView.as_view(), name='my-order-update'),
    path('myorders/<int:pk>/delete', views.UzsakymoEiluteByUserDeleteView.as_view(), name='my-order-delete')
]