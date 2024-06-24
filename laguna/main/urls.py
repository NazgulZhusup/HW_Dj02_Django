
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('first', views.first, name='page1'),
    path('second', views.second, name='page2'),
    path('third', views.third, name='page3')
]