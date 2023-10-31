from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .models import timezone
from .forms import ItemForm
from django.contrib.auth.decorators import login_required

@login_required
def item_list(request):
    items = Item.objects.all()
    return render(request, 'itemlist/item_list.html', {'items': items})

@login_required
def create_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return redirect('item_list')
    else:
        form = ItemForm()
    return render(request, 'itemlist/item_form.html', {'form': form})

@login_required
def update_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)

    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            item.date_updated = timezone.now()
            item.user = request.user
            item.save()
            return redirect('item_list')
    else:
        form = ItemForm(instance=item)
    return render(request, 'itemlist/item_form.html', {'form': form, 'item': item})



def logout():
    return redirect()
    pass