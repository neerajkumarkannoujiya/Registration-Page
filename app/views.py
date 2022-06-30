from django.shortcuts import render

# Create your views here.
def RegisterPage(request):
    return render(request,"register.html")
