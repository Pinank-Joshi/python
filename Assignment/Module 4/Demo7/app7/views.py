from django.shortcuts import render, redirect
from .forms import *

# Create your views here.

from .models import userinfo

def index(request):
    error = None
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = userinfo.objects.get(email=email, password=password)
            request.session['user_id'] = user.id
            return redirect('welcome')
        except userinfo.DoesNotExist:
            error = "Invalid Email or Password"

    return render(request, 'index.html', {'error': error})

def signup(request):
    if request.method=='POST':
        form = userinfoform(request.POST)
        if form.is_valid():
            form.save()
            print("Record Inserted")
            return render(request, 'signup.html', {'signup_success': True})
        else:
            print(form.errors)
    return render(request,'signup.html')

def welcome(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('/')
    try:
        user = userinfo.objects.get(id=user_id)
        return render(request, 'welcome.html', {'username': user.name})
    except userinfo.DoesNotExist:
        return redirect('/')

def logout(request):
    if 'user_id' in request.session:
        del request.session['user_id']
    return redirect('/')

def showdata(request):
    userdata = userinfo.objects.all()
    return render(request,'showdata.html',{'userdata':userdata})

def deletedata(request,id):
    user = userinfo.objects.get(id=id)
    user.delete()		
    return redirect('showdata')

def update(request,id):
    user = userinfo.objects.get(id=id)
    if request.method == 'POST':
        form = userinfoform(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('showdata')
        else:
            print(form.errors)
    return render(request, 'update.html', {'profile': user})