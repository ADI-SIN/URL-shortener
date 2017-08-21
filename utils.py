from django.conf import settings
import random
import string

SHORTCODE_MIN = getattr(settings, "SHORTCODE_MIN", 6)

def code_generator(size=SHORTCODE_MIN, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))  
    #shotform of for loop

def create_shortcode(instance, size=SHORTCODE_MIN):
      new_code = code_generator(size=size)
      Klass = instance.__class__   #to get URL class from this function    
      qs = Klass.objects.filter(shortcode=new_code).exists()  #to check if alreadyexists or not
      if qs_exists:
      	return create_shortcode(size=size)
      return new_code
        