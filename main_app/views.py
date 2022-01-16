# from sre_constants import CATEGORY_UNI_DIGIT
from django.shortcuts import render, redirect
# from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Finch, Medicine
# from .models import finches as finches
from .forms import FeedingForm

# Create your views here.


def home(request):
    # return render('<h1>Finch Collector Home Page</h1>')
    return render(request, 'home.html')

def about(request):
    return render(request, "about.html")

def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', { 'finches': finches })

def finches_detail(request, finch_id):
    finches = Finch.objects.get(id=finch_id)
    feeding_form = FeedingForm()
    return render(request, 'finches/detail.html', {
        'finchdetail' : finches,
        'feeding_form': feeding_form 
    })

def add_feeding(request, finch_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.finch_id = finch_id
        new_feeding.save()
    return redirect('finches_detail', finch_id=finch_id)

class MedicineList(ListView):
  model = Medicine


class MedicineDetail(DetailView):
  model = Medicine


class MedicineCreate(CreateView):
  model = Medicine
  fields = '__all__'


class MedicineUpdate(UpdateView):
  model = Medicine
  fields = ['device', 'Side']


class MedicineDelete(DeleteView):
  model = Medicine
  success_url = '/medicines/'



class FinchCreate(CreateView):
    model = Finch
    fields = ['name', 'native', 'description']
    success_url = '/finches/'

class FinchUpdate(UpdateView):
    model = Finch
    fields = ['native', 'description']


class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches/'

