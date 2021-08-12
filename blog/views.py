from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse

# Create your views here.

def home(index):
    return HttpResponse('This is Home')

def blog(index):
    return HttpResponse('This is Blog')