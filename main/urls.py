from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('shop_all/', views.shop_all, name='shop_all'),
    path('ingredients/', views.ingredients, name='ingredients'),
    path('advertisement/', views.advertisement_view, name='advertisement'),
]
