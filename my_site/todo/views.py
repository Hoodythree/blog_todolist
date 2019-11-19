from django.shortcuts import render, redirect
from .models import List
from django.http import HttpResponse
# Create your views here.
from .forms import ListForm
from django.contrib import messages


def index(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = List.objects.all
            messages.success(request, ('Item Has Been Added To List'))
            return render(request, 'todo/index.html', {'all_items': all_items})

    else:
        all_items = List.objects.all
        return render(request, 'todo/index.html', {'all_items': all_items})


def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    # mark
    messages.success(request, ('Item has been deleted'))
    return redirect('todo:index')


def cross_off(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = True
    item.save()
    return redirect('todo:index')


def uncross(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = False
    item.save()
    return redirect('todo:index')
