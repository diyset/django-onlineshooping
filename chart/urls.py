from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.detail_cart, name='cart_detail'),
    path('add/<int:product_id>/', views.add_cart, name='add_cart'),
    path('remove/<int:product_id>/', views.remove_cart, name='cart_remove'),

]
