from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def basic(request):
    return HttpResponse("This is my second Django Server")


def second(request):
    return render(request, "second_app/index.html") 