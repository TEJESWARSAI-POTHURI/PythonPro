from django.contrib.sites import requests
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
import random, string

from userapp.forms import Datetime

from .forms import PieChartForm


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
    return render(request, 'submit_form.html')

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
        username=request.POST.get('username')
        password=request.POST.get('password')
        logintb.objects.create(username=username,password=password)
        return redirect('submit_form')
    return render(request,'login')

def pie(request):
    return render(request,'piechart.html')

import matplotlib.pyplot as plt
import numpy as np

def pie_chart(request):
    if request.method == 'POST':
        form = PieChartForm(request.POST)
        if form.is_valid():
            # Process user input
            y_values = [int(val) for val in form.cleaned_data['y_values'].split(',')]
            labels = [label.strip() for label in form.cleaned_data['labels'].split(',')]

            # Create pie chart
            plt.pie(y_values, labels=labels, startangle=90)
            plt.savefig('static/images/pie_chart.png')  # Save the chart image
            img1={'chart_image': '/static/images/pie_chart.png'}
            return render(request, 'piechart.html', img1)
    else:
        form = PieChartForm()
    return render(request, 'piechart.html', {'form': form})


def cars(request):
    return render(request,'services.html')
import requests
def weather(request):
    return render(request,'weather.html')

def weatherboarding(request):
        if request.method == 'POST':
            place = request.POST['place']
            API_KEY = 'a314b8b8c6e4602ee39e7400ed68fe03'
            url = f'http://api.openweathermap.org/data/2.5/weather?q={place}&appid={API_KEY}'
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                temperature = data['main']['temp']
                humidity = data['main']['humidity']
                temperature1 = round(temperature - 273.15, 2)
                return render(request, 'weather.html',
                              {'city': str.upper(place), 'temperature1': temperature1, 'humidity': humidity})
            else:
                error_message = 'City not found. Please try again.'
                return render(request, 'weather.html', {'error_message': error_message})

def feedback(request):
    return render(request,'feedback.html')


def feeddata(request):
    name=request.POST.get('name')
    email=request.POST.get('email')
    message=request.POST.get('message')
    data=feedmail.objects.create(name=name,email=email,message=message)
    data.save()

    recipient_email =email
    subject = 'Thanks for submitting your Feed Back'  # Set your subject here
    message_body = message  # Set your email content here
    send_mail(
        subject,
        message_body,
        '2200031690cseh@gmail.com',
        [recipient_email],
        fail_silently=False,
    )
    return render(request,'feedback.html')