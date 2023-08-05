from django.shortcuts import render,HttpResponse
from .models import ContactTb
# Create your views here.

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def all_blogs(request):
    return render(request,'all_blogs.html')

def contact(request):

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['add']
        message = request.POST['msg']

        # if len(name) > 1 and len(email) >15 and len(str(phone)) == 10 and len(address) > 15 and len(message) > 20:
        contactObj = ContactTb(name=name,
                                email=email, phone=phone,
                                address=address,message=message,)
        contactObj.save()

        # else :
        #     return HttpResponse('Please fill valid information.')
    return render(request,'contact.html')