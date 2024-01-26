from django.http import HttpResponse 
from django.contrib.auth.models import User
from django.shortcuts import render , redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from main_app.admin import contact 
from main_app.admin import services
from main_app.admin import slider
from main_app.admin import staff
from main_app.admin import category_rooms

def indexpage(request):
        
    sliderdata =slider.objects.all()
    
    staffdata=staff.objects.all()
    
    category_roomsdata=category_rooms.objects.all()
    
    servicesdata=services.objects.all()
    data={
        'servicesdata':servicesdata,
        'sliderdata':sliderdata,
        'staffdata':staffdata,
        'category_roomsdata':category_roomsdata
    }
    
    # if request.method=="POST":
    #     name=request.POST.get('name')
    #     email=request.POST.get('email')
    #     phone_no=request.POST.get('phone_no')
    #     # p=request.POST.get('p')
    #     address=request.POST.get('address')
    #     pincode=request.POST.get('pincode')
    #     birth=request.POST.get('birth')
    #     password=request.POST.get('password')
    #     confirm_password=request.POST.get('confirm_password')

    #     registerdata=user(name=name,email=email,phone_no=phone_no,address=address,pincode=pincode,birth=birth,password=password,confirm_password=confirm_password)
    #     registerdata.save()
        # return render(request,"index.html")
    return render(request,"index.html",data)

def aboutuspage(request):
    return render(request,"about-us.html")

def contactpage(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        contact_deta=contact(name=name,email=email,message=message)
        contact_deta.save()
    return render(request,"contact.html")

def roompage(request):
    return render(request,"room.html")

def your_bookingpage(request):
    return render(request,"your_booking.html")


def hendleregister(request):
     if request.method=="POST":
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        username=request.POST.get('createusername')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        
        if password != confirm_password:
            messages.error(request,"password do not match")
            return redirect('index')
        
        myuser=User.objects.create_user(username,email,password)
        myuser.first_name=firstname
        myuser.last_name=lastname
        myuser.save()
        messages.success(request,"register")
        return redirect('index')
     
        
     else:
        return HttpResponse('404 page')
    
     

def handlelogin(request):
    if request.method == 'POST':
        loginusername=request.POST.get('loginusername')
        loginpassword=request.POST.get('loginpassword')
                 
        user = authenticate(username=loginusername, password=loginpassword)
        
        if user is not None:
            login(request,user)
            messages.success(request,"login")
            return redirect('index')
        else:
            messages.error(request,"not login")
            return redirect('index')
        
    return HttpResponse('404 page')

def handlelogout(request):
        logout(request)
        messages.success(request,"logout success")
        return redirect('index')
