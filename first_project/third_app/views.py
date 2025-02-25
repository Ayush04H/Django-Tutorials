from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def third(request):
    return render(request,"third_app/index.html")