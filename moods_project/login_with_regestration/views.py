from django.shortcuts import render,HttpResponse

from pytz import all_timezones #importing all time zones in the pyz library

# Create your views here.

# referring to the main login method
def index(request):
  return render(request, "login.html")


# referring to the main regestration page 
def show_registration_page(request):
  time_zones = all_timezones
  
  context = {'time_zones': time_zones}
  return render(request,"register.html",context)


# def my_view(request):
#     time_zones = all_timezones
#     context = {'time_zones': time_zones}
#     return render(request, 'my_template.html', context)