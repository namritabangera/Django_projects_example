from django.urls import path
from app1.views import *

urlpatterns= [
path('index/',indexview),
path('products/',products),
]

