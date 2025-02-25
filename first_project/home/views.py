from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
'''def home(request):
    return HttpResponse("<h1>This is My Django Server ! Welcome to the First Program</>")'''

def home(request):
    return render(request,"index.html")


def test(request):
    return HttpResponse("This is Another Function of the Django")
