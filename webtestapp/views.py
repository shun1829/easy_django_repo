from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("That's the life!")