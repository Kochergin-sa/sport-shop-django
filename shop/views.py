from django.shortcuts import render

def home(request):
    return render(request, 'shop/home.html')

def catalog(request):
    return render(request, 'shop/catalog.html')

def about(request):
    return render(request, 'shop/about.html')