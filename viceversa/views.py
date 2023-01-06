from django.http import HttpResponse
from django.shortcuts import render

#def about1(request):
#    return HttpResponse('This is about page')

def home(request):
    return render(request,'home.html')
