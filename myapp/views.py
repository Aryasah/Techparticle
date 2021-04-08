from django.shortcuts import render,redirect 
from .forms import ImageForm,ReviewForm,FbForm
from .models import Image
from .models import Images
from .models import Review
from .models import FbPost


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
    
    print("ad")
    form = ImageForm()
    img = Image.objects.all()
    uname = request.POST.get('name')
        
    email_contact = request.POST.get('email')
    sub = request.POST.get('subject')
    message_contact = request.POST.get('message')
        
    contact_us=Contact(contact_name=uname,contact_email= email_contact,contact_message=message_contact,contact_subject=sub)
    contact_us.save()
    print(contact_us)
    messages.success(request, 'Your message has been sent!')

  return  redirect('/')
  
        
     
