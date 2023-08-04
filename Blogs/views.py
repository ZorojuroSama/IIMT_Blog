from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def all_blogs(request):
    return render(request,'all_blogs.html')

def contact(request):
    return render(request,'contact.html')