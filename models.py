from django.conf import settings
from django.db import models
from django.utils import timezone
from .utils import code_generator, create_shortcode

from .validators import validate_url, validate_dot_com


SHORTCODE_MAX = getattr(settings, "SHORTCODE_MAX", 15)
#we can write SHORTCODE_MAX = settings.SHORTCODE_MAX, but the above syntax is preffered

class URLmanager(models.Manager):
    def all(self, *args, **kwargs):
        #default constructor that shows all the objects, we will edit it to show only active urls, this is called managing models
        qs_main = super(URLmanager, self).all(*args, **kwargs)
        qs = qs_main.filter(active=True)
        return qs

    def refresh_shortcode(self): #our function to refresh/edit shotcode
      qs = URL.objects.filter(id__gte=1)   #this is actual all() method, give all objects er than owhose id is greater than or equal to one(gte)
      for q in qs:
          q.shortcode = create_shortcode(q) #refreshing shortcodes
          q.save     


class URL(models.Model):
    
    url = models.CharField(max_length=220,validators=[validate_url, validate_dot_com])
    shortcode = models.CharField(max_length=SHORTCODE_MAX,unique=True,blank=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    
    obj = URLmanager()

    #this is already a method used to save in database, here we are overriding it
    def save(self, *args, **kwargs):   
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = create_shortcode(self)
        super(URL,self).save(*args, **kwargs)  
        #this constuctor automatically calls save function

    def __str__(self):
        return self.url

      

#python manage.py makemigrations
#python manage.py migrate