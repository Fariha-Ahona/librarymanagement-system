from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def explore(request):
    return render(request, 'explore.html')
