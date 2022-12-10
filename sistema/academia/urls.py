from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home' ),
    path('estudiante/home', views.casa_estudiante, name = 'casa_estudiante')
]

