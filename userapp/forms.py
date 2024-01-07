from django import forms
import datetime

class Datetime(forms.Form):
    text=forms.IntegerField()
    date_value=forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
