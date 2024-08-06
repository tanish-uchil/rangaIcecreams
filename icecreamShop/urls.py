from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('shop/', views.shop, name='shop'),
    path('profile/', views.profile, name='profile'),
    path('cart/', views.cart, name='cart'),
    path('updateUser/',views.updateUser, name='updateUser')
]
