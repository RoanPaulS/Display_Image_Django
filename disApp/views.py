from django.shortcuts import render
from django.http import HttpResponse

def display(request):
    return render(request,'homeDI.html')

