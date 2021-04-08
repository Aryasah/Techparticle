from django.db import models

# Create your models here.
class Image(models.Model):
 
 photo = models.ImageField(upload_to="myimage")
 date = models.DateTimeField(auto_now_add=True)
 name= models.CharField(max_length=122,blank=True,null=True)
 position=models.CharField( max_length=50,blank=True,null=True)

class Contact(models.Model):
    
    contact_name= models.CharField(max_length=122,blank=True,null=True)
    contact_subject= models.CharField(max_length=122,blank=True,null=True)
    contact_email= models.EmailField(max_length=122,blank=True,null=True)
    contact_message= models.CharField(max_length=122,blank=True,null=True)

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

    
