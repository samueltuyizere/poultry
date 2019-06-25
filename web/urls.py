from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='Home'),
    path('product/<id>/', product, name='Product'),
    path('products/', products, name='Products'),
    path('posts/', posts, name='Posts'),
    path('post/<id>/', post, name='Post'),
]