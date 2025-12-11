from django.urls import path
from app1.views import *

urlpatterns=[
    path('view1/',view1),
    path('view2/',view2),
]