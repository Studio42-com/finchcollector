from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>What the Finch you looking at?</h1>')

def about(request):
    # return HttpResponse('<h1>About this feather-brained imbecile</h1>')
    return render(request, "about.html")

def finches_index(request):
    return HttpResponse("<h1>It's all about the Finches</h1>")
