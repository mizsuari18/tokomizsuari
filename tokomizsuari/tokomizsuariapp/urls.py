from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.landing, name='landing'),
    path('<int:id>', views.detail, name='detail'),
    path('contact/', views.contact, name='contact')
]