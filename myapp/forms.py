from django import forms
from .models import Image,Review

class ImageForm(forms.ModelForm):
 class Meta:
  model = Image
  fields = '__all__'
  labels = {'photo':''}

class ReviewForm(forms.ModelForm):
 class Meta:
  model = Review
  fields = '__all__'
  labels = {'photos':''}
  