from django.shortcuts import render
from .models import Item

# Create your views here.

def home(request):
    shop = Item.objects.all()
    return render(request, 'home.html', {'shop':shop})

def create(request):
    # 강의를 따라 완성해봅시다.
    pass

def update(request, item_id):
    # 강의를 따라 완성해봅시다.
    pass

def delete(request, item_id):
    # 강의를 따라 완성해봅시다.
    pass