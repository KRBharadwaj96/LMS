from django.db import models

# Create your models here.
class CModulesDB(models.Model):
    NewModule = models.CharField(max_length=100,null=True,blank=True)
    Subject = models.CharField(max_length=100,null=True,blank=True)
    Material = models.CharField(max_length=100,null=True,blank=True)
    Image = models.ImageField(upload_to='module',null=True,blank=True)
    Files = models.FileField(upload_to='files',max_length=250)
    Select = models.CharField(max_length=100,null=True,blank=True)

class LessonDB(models.Model):
    SubName = models.CharField(max_length=200,null=True,blank=True)
    LImage = models.ImageField(upload_to='Lesson',null=True,blank=True)
    LessonName = models.CharField(max_length=200,null=True,blank=True)
    Videos = models.FileField(upload_to='videos',max_length=250,null=True,blank=True)
    Study_m = models.FileField(upload_to='Materials',null=True,blank=True)
