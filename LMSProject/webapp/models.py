from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Registerdb(models.Model):
    Name = models.CharField(max_length=200,blank=True,null=True)
    Email = models.EmailField(max_length=400,blank=True,null=True)

    Password = models.CharField(max_length=100,null=True,blank=True)



class Usersubmitdb(models.Model):
    Uname = models.CharField(max_length=200,blank=True,null=True)
    Modname = models.CharField(max_length=200,blank=True,null=True)
    Name = models.CharField(max_length=200,blank=True,null=True)
    Email = models.EmailField(max_length=200,blank=True,null=True)
    Comments = models.CharField(max_length=500,blank=True,null=True)
    Upload = models.FileField(upload_to='Submit',max_length=250)

class Contactdb(models.Model):
    Message = models.CharField(max_length=500,null=True,blank=True)
    Name = models.CharField(max_length=100,null=True,blank=True)
    Email = models.EmailField(max_length=150,null=True,blank=True)
    Subject = models.CharField(max_length=100,null=True,blank=True)
