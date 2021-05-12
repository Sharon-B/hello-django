from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm


# Create your views here.
# Get items:
def get_todo_list(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)


# Add items:
def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_todo_list')
   
    form = ItemForm()
    context = {
        'form': form
    }

    return render(request, 'todo/add_item.html', context=context)
