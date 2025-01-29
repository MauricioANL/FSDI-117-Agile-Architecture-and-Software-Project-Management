from django.urls import path
from . import views

urlpatterns = [
    path('', views.about_view, name='about'),
    # path('pages/', views.about_view, name='about'),  # Página de inicio
]
