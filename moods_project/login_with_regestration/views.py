from django.shortcuts import render,HttpResponse

# Create your views here.

# referring to the main test method 
def index(request):
  return HttpResponse("you have successfully confugured your app!")
