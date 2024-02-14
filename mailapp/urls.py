""
from django.contrib import admin
from django.urls import path,include

from .views import send_emails

urlpatterns = [
    path('',send_emails, name="email"),


]