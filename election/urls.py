from django.urls import path
from .views import *

app_name = 'election'

urlpatterns = [
    path('', home, name='home'),
    path('lga/', lga, name='lga'),
    path('add/', addpage, name='addpage'),
]
