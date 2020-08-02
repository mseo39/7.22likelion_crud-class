from django.shortcuts import render, get_object_or_404, redirect
from .models import Item

# Create your views here.

def home(request):
    shop = Item.objects.all()
    return render(request, 'home.html', {'shop':shop})

def create(request):
    if request.method == 'POST':
        item=Item()
        item.name=request.POST['name']
        item.price=request.POST['price']

        item.save()
        return redirect('home')
    

def update(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if request.method == 'POST':
        item.name=request.POST['name']
        item.price=request.POST['price']
        item.save()
        return redirect('home')
    else:
        return render(request, 'update.html',{'items':item})

def delete(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    item.delete()
    return redirect('home')