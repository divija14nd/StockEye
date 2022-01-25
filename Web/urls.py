from django.urls import path
from . import views

# ------------------------ Importing URLS for the pages ------------------------ #

urlpatterns = [
    path('',views.home, name='home'),
    path('detail/', views.detail, name = 'detail'),
    path('search-stock',views.search_stock, name='search_stock')
]
