from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def templates(request):

    peoples = [
        {'name':'Ayush','age':20},
        {'name':'Piyush','age':15},
        {'name':'Sumit','age':20},
        {'name':'Prabhat','age':20},
        {'name':'Pandu','age':20},
        {'name': 'Radha', 'age': 25},
    {'name': 'Krishna', 'age': 30},
    {'name': 'Gopal', 'age': 18},
    {'name': 'Meera', 'age': 22},
    {'name': 'Arjun', 'age': 28},
    {'name': 'Bheem', 'age': 35},
    {'name': 'Nakul', 'age': 19},
    {'name': 'Sahdev', 'age': 21},
    {'name': 'Yudhisthir', 'age': 40},
    {'name': 'Draupadi', 'age': 32},
    {'name': 'Karna', 'age': 27},
    {'name': 'Abhimanyu', 'age': 16},
    {'name': 'Dhritarashtra', 'age': 60},
    {'name': 'Gandhari', 'age': 58},
    {'name': 'Vidur', 'age': 45},
    {'name': 'Sanjay', 'age': 33},
    {'name': 'Duryodhan', 'age': 29},
    {'name': 'Dushasan', 'age': 26},
    {'name': 'Shakuni', 'age': 50},
    {'name': 'Kunti', 'age': 55},
    ]
    return render(request,"django_temp/index.html",context= {'peoples':peoples})