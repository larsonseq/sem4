from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from django.contrib.auth import authenticate, login
 

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                return render(request, 'sign_up.html', {'error': 'Username is already taken'})
            
            user = User.objects.create(username=username, first_name=first_name, last_name=last_name, passw=password1)
            # user.set_password(password1)
            # user.save()
            
            return redirect('login')
        else:
            return render(request, 'sign_up.html', {'error': 'Passwords do not match'}) 
    
    return render(request, 'sign_up.html')
 

def user_login(request):
    if request.method == 'POST':
        context = {}
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.authenticate(username=username, passw=password)

        if user is not None:
            login(request, user)
            return redirect('next')
        else:
            context.update({'loginerror':"invalid credentials"})
            print(context)
            return render(request, 'login.html', context=context)
    
    return render(request, 'login.html')

def next(request):
    return render(request, 'next.html')
