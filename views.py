from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import URL
from .forms import SubmitUrlForm
# a function and a class is defined to manage views, both will perform the same function


class HomeView(View):    #html page view
   def get(self, request, *args, **kwargs):
       the_form = SubmitUrlForm()
       context = {
       "title": "Submit URL",
       "form": the_form
       }
       return render(request, "Myblog/home.html", context)


   def post(self, request, *args, **kwargs):
         form = SubmitUrlForm(request.POST)
         context = {
         "title": "Submit URL",
         "form": form
         }
         return render(request, "Myblog/home.html",context)
      








def redirect_view(request, shortcode=None, *args, **kwargs):   #function based view manages get and post methods by default
   

    objj = get_object_or_404(URL, shortcode=shortcode)
     
    #return HttpResponse("hello {sc}".format(sc=objj.url))
      
    #built in method to redirect to link  
    return HttpResponseRedirect(objj.url)          



class RedirectView(View):                                                 #class based view needs to define get and post methods separately
 def get(self, request, shortcode=None, *args, **kwargs):
     objj = get_object_or_404(URL, shortcode=shortcode)
     #return HttpResponse("hello again {sc}".format(sc=shortcode)) 
     return HttpResponseRedirect(objj.url) 
 
 def post(self, request,*args, **kwargs):
      return HttpResponse()    




    # objj = get_object_or_404(URL, shortcode=shortcode)                      the code which is throwing error in function redirect_view

    # try: 
    #     obj = URL.objects.get(shortcode=shortcode)
    # except:
    #     obj = URL.objects.all.first() 

   
    # obj_url = None
    # query = URL.objects.filter(shortcode__iexact=shortcode.upper())
    #  if query.exists() and query.count() == 1:
    #    query = query.first()
    #    obj_url = obj.url 
 
    # return HttpResponse("hello {sc}".format(sc=objj.url))
     