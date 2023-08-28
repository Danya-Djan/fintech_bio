# myapp/views.py
from django.shortcuts import render, redirect

def login_page(request):
    return render(request, 'login.html')

def pdf_page(request):
    return render(request, 'pdf.html')

def voice_page(request):
    return render(request, 'voice.html')
