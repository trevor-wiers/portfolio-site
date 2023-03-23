from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('home', views.home, name="home"),
    path('grit-eq', views.gritEQ, name="gritEQ"),
    path('spectro', views.spectro, name="spectro")
]