from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Finch

# Create your views here.
from django.http import HttpResponse

def home(request):
    # return render('<h1>Finch Collector Home Page</h1>')
    return render(request, 'home.html')

def about(request):
    return render(request, "about.html")

def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', { 'xyzfinches': finches })

def finches_details(request, finch_id):
    finches = Finch.objects.get(id=finch_id)
    return render(request, 'finches/detail.html', { 'detail' : finches })

class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'
    success_url = '/finches/'

class FinchUpdate(UpdateView):
    model = Finch
    fields = ['native', 'description']


class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches/'

