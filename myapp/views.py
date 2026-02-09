from django.shortcuts import render
from .models import Item

# Create your views here.
def home(request):
    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')