from django.db import models
from datetime import datetime

# Create your models here.
class Image(models.Model):
 
 photo = models.ImageField(upload_to="myimage")
 date = models.DateTimeField(auto_now_add=True)
 name= models.CharField(max_length=122,blank=True,null=True)
 position=models.CharField( max_length=50,blank=True,null=True)

class Contact(models.Model):
    name = models.CharField(max_length=122,blank=True,null=True)
    email = models.CharField(max_length=122,blank=True,null=True)
    phone = models.CharField(max_length=12,blank=True,null=True)
    desc = models.TextField(default="none",blank=True,null=True)
    date = models.DateTimeField(auto_now_add=True)
class Images(models.Model):
    photos = models.ImageField(upload_to="myimages")
    dates = models.DateTimeField(auto_now_add=True)
    
class FbPost(models.Model):
    post = models.ImageField(upload_to="fbpost")
    datess = models.DateTimeField(auto_now_add=True)

class Review(models.Model):
 
 time = models.DateTimeField(auto_now_add=True)
 username= models.CharField(max_length=122,blank=True,null=True)
 profession=models.CharField( max_length=50,blank=True,null=True)
 comment= models.CharField(max_length=122,blank=True,null=True)
 picture = models.ImageField(upload_to="user")

    
