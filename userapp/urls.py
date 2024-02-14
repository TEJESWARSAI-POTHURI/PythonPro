from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [

    path('', homepage, name="Homepage"),
    path('travels/', travelpkg, name="travelpkg"),
    path('print/', print1, name='print'),
    path('form/',print_to_console,name="submit_form"),
    path('print2/', print1, name='print2'),
    path('otp/', printconsole, name="randomOTP"),
    path('date/', dates,name='datefile'),
    path('dankar/',get_date,name='dankar'),
    path('regf/',reg,name='register'),
    path('check/',regfun,name='check'),
    path('logins/',login,name='logins'),
    path('checklogins/',logins,name='checklog'),
    path('piechart/', pie_chart,name='piechart'),
    path('pie/',pie,name='pie'),
    path('cars',cars,name='cars'),
    path('weather/',weather,name='weather'),
    path('weather1/',weatherboarding,name='weather1'),
    path('feedback/',feedback,name='feedback'),
    path('feeddata/',feeddata,name='feeddata')
]
