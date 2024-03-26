from django.shortcuts import render
from .models import Product

# Create your views here.

def landing(request):
    # dictionary for initial data with 
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["dataset"] = Product.objects.all()
    return render(request, "index.html", context)


def detail(request, id):
    # dictionary for initial data with 
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["data"] = Product.objects.get(id = id)   
    return render(request, "product.html", context)

def contact(request):
    # dictionary for initial data with 
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["dataset"] = Product.objects.all()
    return render(request, "contact.html", context)


