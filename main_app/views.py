from django.shortcuts import render
from .models import Finch

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Finch Collector Home Page</h1>')

def about(request):
    return render(request, "about.html")

def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', { 'xyzfinches': finches })

def finches_details(request, finch_id):
    finches = Finch.objects.get(id=finch_id)
    return render(request, 'finches/detail.html', { 'detail' : finches })
