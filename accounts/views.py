from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method == 'POST':
        # the user has info and wants an account now
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error':'Username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], request.POST['password1'])
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html', {'error':'Passwords must match.'})
    else:
        # the user wants to sign in
        return render(request, 'accounts/signup.html')
    
def login(request):
    return render(request, 'accounts/login.html')

def logout(request):
    # TODO need to route to home page
    # and don't forget to logout :)
    return render(request, 'accounts/signup.html')
