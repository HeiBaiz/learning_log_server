from django.shortcuts import render

# Create your views here.

def index(request):
    """learning_plans主页"""
    return render(request, 'learning_plans/index.html')
