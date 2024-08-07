from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import StoreManagerSignUp_Form
from django.template import loader
from .models import StoreManager
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages

# Create your views here.

def sign_up(request):
    if request.method == 'POST':
        form = StoreManagerSignUp_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('template')
    else:
        form = StoreManagerSignUp_Form()

    return render(request, 'signup.html', {'form':form})

def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = StoreManager.objects.get(email=email)
            if user.password == password:
                auth_login(request, user)
                return redirect('template')
            else:
                messages.error(request, 'Invalid credentials')
        except StoreManager.DoesNotExist:
            messages.error(request, 'Invalid credentials')
        
    return render(request, user.html)

def testing(request):
    template = loader.get_template('template.html')
    users = StoreManager.objects.all().values()
    context = {
        'users': users,
    }
    return HttpResponse(template.render(context, request))