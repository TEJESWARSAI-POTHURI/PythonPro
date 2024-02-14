from django.db import models
#this is for registration
# Create your models here.
class Teja(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(primary_key=True)
    password=models.CharField(max_length=100)
    phonenumber=models.IntegerField()

    class Meta:
        db_table = "Sankar"  # To show the table name to the user
# this is login page
class logintb(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=8)

    class Meta:
        db_table ="logins"

#this is for feedback



class feedmail(models.Model):

    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    message = models.CharField(max_length=100)

    class Meta:
        db_table="feedmail"