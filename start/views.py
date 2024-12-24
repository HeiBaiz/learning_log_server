from django.shortcuts import render

# Create your views here.

def index(request):
    """导航主页"""
    return render(request, 'start/index.html')
