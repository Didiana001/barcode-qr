from django.urls import path
from .views import home, add_product

urlpatterns = [
    path('', home, name='home'),  # Home page
    path('add_product/', add_product, name='add_product'),  # URL to add a product
]
