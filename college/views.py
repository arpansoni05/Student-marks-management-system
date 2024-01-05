from django.shortcuts import render
# Create your views here.

def home(request):
    return render(request, 'index.html')

def college1(request):
    return render(request, 'college/college.html')

# views.py


