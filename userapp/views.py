from django.http import HttpResponse
from django.shortcuts import render, redirect
import random, string

from userapp.forms import Datetime


# Create your views here.
def hello(request):
    return HttpResponse("<center> HELLO </center>")


def homepage(request):
    return render(request, 'Homepage.html')


def travelpkg(request):
    return render(request, 'travelpkg.html')


def print1(request):
    return render(request, 'submit_form.html')


def print_to_console(request):
    if request.method == 'POST':
        user_input = request.POST['user_input']
        print(f'user_input:{user_input}')
        # return HTTPResponse("form submitted successfully")
        a1 = {'user_input': user_input}
        return render(request, 'submit_form.html', a1)


def printotp(request):
    return render(request, 'submit_form.html')


def printconsole(request):
    s = 4  # this one gives the no of characters
    ran = ''.join(random.sample(string.digits, k=s))
    print(f'OTP: {ran}')
    a1 = {'randomguys': ran}
    return render(request, 'randomOTP.html', a1)

def dates(request):
    return render(request,'datefile.html')

import datetime
from django.shortcuts import render


def get_date(request):
    if request.method == 'POST':
        form = Datetime(request.POST)
        if form.is_valid():
            integer_value = form.cleaned_data['text']
            date_value = form.cleaned_data['date_value']
            updated_date = date_value + datetime.timedelta(days=integer_value)
            return render(request, 'datefile.html', {'updated_date': updated_date})
        else:
            form = Datetime()
            return render(request, 'datefile.html', {'form': form})

def reg(request):
    return render(request,'Register.html')

from .models import *

def regfun(request):
    if(request.method=='POST'):
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        phonenumber=request.POST.get('phonenumber')

        if Teja.objects.filter(email=email).exists():
            return HttpResponse("Email is already registred chose another mail")
        Teja.objects.create(name=name,email=email,password=password,phonenumber=phonenumber)
        return redirect('Homepage')
    return render(request,'Register')
def login(request):
    return render(request,'login.html')

from .models import *
def logins(request):
    if(request.method=='POST'):
        username=request.POST.get('Username')
        password=request.POST.get('Password')

        if logintb.objects.filter(username=username).exists():
            return HttpResponse("username already registred chose another mail")
        logintb.objects.create(username=username,password=password)
        return redirect('submit_form')
    return render(request,'login')