from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.index, name='index'),
    path('crear_autor/', views.crear_autor, name='crear_autor'),
]
