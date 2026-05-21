from django.urls import path
from .views import kaart_view

urlpatterns = [
    path('', kaart_view, name='kaart'),
]