from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('notes', views.about, name='about'),
]