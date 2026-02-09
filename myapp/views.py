from django.shortcuts import render, get_object_or_404
from .models import Item

# Create your views here.
def home(request):
    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def item_detail(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    return render(request, 'item_detail.html', {'item': item})
