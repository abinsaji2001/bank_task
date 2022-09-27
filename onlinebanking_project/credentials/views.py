from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['Password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('button')
        else:
            messages.info(request, "invalid credentials")
            return redirect('login')
    return render(request, "login.html")


def register(request):
    if request.method == 'POST':
        username = request.POST['Username']

        password = request.POST['Password']
        cpassword = request.POST['Password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect('register')

            else:
                user = User.objects.create_user(username=username, password=password)
                user.save();
                return redirect('login')

        else:
            messages.info(request, "password not matching")
            return redirect('register')
        return redirect('/')
    return render(request, "register.html")


def form(request):
    if request.method == 'POST':
        username = request.POST['Username']

        user = auth.authenticate(username=username)
        if user is not None:
            messages.info(request, 'Application accepted')
            return redirect('form')
        else:
            return redirect('application')
    else:
        return render(request, "form.html")

    return render(request, 'form.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def application(request):
    return render(request, 'application.html')

def button(request):
    return render(request,'button.html')
