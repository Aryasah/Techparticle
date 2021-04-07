from django.contrib import admin
from .models import Image
from .models import Images
from .models import Contact
from .models import Review
# Register your models here.

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
 list_display = ['id', 'photo', 'date','name','position']

@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
 list_display = ['id', 'photos', 'dates']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
 list_display = ['id', 'picture', 'username', 'profession','comment']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
 list_display = ['id', 'contact_name','contact_email','contact_subject','contact_message']
