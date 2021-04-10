from django.shortcuts import render,redirect 
from .forms import ImageForm,ReviewForm,FbForm
from .models import Image
from .models import Images
from .models import Review
from .models import FbPost
from datetime import datetime
from django.conf import settings
from django.core.mail import send_mail


from .models import Contact
from django.contrib import messages

# Create your views here.
imag=''
forms=''
formes=''
image=''


def home(request):
 
 if request.method == "POST":
  form = ImageForm(request.POST, request.FILES)
  if form.is_valid():
   form.save()
  
 form = ImageForm()
 img = Image.objects.all()
 imgs =Images.objects.all()
 global imag
 global forms
 global formes
 global image
 imag=Review.objects.all()
 forms = ReviewForm()
 image = FbPost.objects.all()
 
 formes=FbForm()
 
 return render(request, 'myapp/home.html', {'imag':imag, 'forms':forms,'img':img, 'form':form ,'imgs':imgs,'formes':formes,'image':image })

def comments(request):
  global forms
  if request.method == "POST":
   forms = ReviewForm(request.POST, request.FILES)
  if forms.is_valid():
   forms.save()
  forms = ReviewForm()
  global imag
  imag=Review.objects.all()
  messages.success(request, 'Thank You For Your Reviews It is submitted succesfully')
  subject = 'Thank You For Contacting TechArya '
  message = f' Your feedback is very much appreciated. We greatly appreciate the time you took to review us. You can go to https://techaryasah.herokuapp.com/ '
  email_from = settings.EMAIL_HOST_USER
  recipient_list = ['aryasah30@gmail.com']
  send_mail(subject, message , email_from ,recipient_list) 
  
  return  redirect('/')

def facepost(request):
  global formes
  if request.method == "POST":
   formes = FbForm(request.POST, request.FILES)
  if formes.is_valid():
   formes.save()
  formes = FbForm()
  global image
  image=FbPost.objects.all()
  messages.success(request, 'Thank You For Your Reviews It is submitted succesfully')
  
  return  redirect('/')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
        subject = 'Thank You For Contacting TechArya '
        message = f'Dear {name} : Thank you for contacting with us. We greatly appreciate the time you took to contact us we will soon reach you with reply. You can go to https://techaryasah.herokuapp.com/ '
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['aryasah30@gmail.com']
        send_mail(subject, message , email_from ,recipient_list ) 
        messages.success(request, 'Your message has been sent!')
    return redirect('/')
  
        
     
