from sre_constants import CATEGORY_UNI_DIGIT
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
    finchdetail = Finch.objects.get(id=finch_id)
    #Get the listing of medical treatments available.
    medicines_finch_doesnt_have = Medicine.objects.exclude(id__in=finchdetail.medicines.all().values_list('id'))
    feeding_form = FeedingForm()
    return render(request, 'finches/detail.html', {
        'finchdetail' : finchdetail,
        'feeding_form': feeding_form,
        #and the treatments to be displayed
        'medicines': medicines_finch_doesnt_have 
    })

def add_feeding(request, finch_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.finch_id = finch_id
        new_feeding.save()
    return redirect('finches_detail', finch_id=finch_id)

def assoc_medicine(request, finch_id, medicine_id):
  finchmeds = Finch.objects.get(id=finch_id)
  finchmeds.medicines.add(medicine_id)
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
  fields = ['medicine']


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

# # Display list of not currently used medical
# def finches_detail(request, finchdetail_id):
#   cat = Cat.objects.get(id=finchdetail_id)
#   # Get the toys the cat doesn't have
#   medicines_finchdetail_doesnt_have = Medicine.objects.exclude(id__in=finchdetail.medicines.all().values_list('id'))
#   feeding_form = FeedingForm()
#   return render(request, 'finches/detail.html', {
#     'finchdetail': finch, 'feeding_form': feeding_form,
#     # Add the toys to be displayed
#     'medicines': medicines_finchdetail_doesnt_have
#   })