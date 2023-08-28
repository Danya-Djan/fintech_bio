# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_page, name='login'),
    path('pdf/', views.pdf_page, name='pdf'),
    path('voice/', views.voice_page, name='voice'),
]
