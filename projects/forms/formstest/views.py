from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .forms import TestForm

def index(request):
    
    return render(request, 'formstest/form.html')

def home(request):
    form = TestForm(request.POST or None)
    if form.is_valid():
        print (form.cleaned_data)
    context = {
        'form': form 
    }
    return render(request, 'formstest/form.html', context)