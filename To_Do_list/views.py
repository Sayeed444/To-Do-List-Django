from django.shortcuts import render,redirect
from .models import List
from .forms import ListForm
from django.contrib import messages
# Create your views here.

def home(request):
    if request.method =='POST':
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save()
            lists = List.objects.all()
            messages.success(request,('Add to To-Do List'))
            return render(request, 'home/home.html', {'lists': lists})

    else:
        lists =List.objects.all()
        return render(request,'home/home.html',{'lists':lists})


def edit(request,list_id):
    if request.method =='POST':
        item = List.objects.get(pk=list_id)
        form = ListForm(request.POST or None,instance=item)
        if form.is_valid():
            form.save()
            messages.success(request,('Edit to To-Do List'))
            return redirect('home')

    else:
        lists =List.objects.get(pk=list_id)
        return render(request,'home/edit.html',{'lists':lists})

def delete(request,list_id):
    list = List.objects.get(pk =list_id)
    list.delete()
    messages.success(request,('Delete to To-Do List'))
    return redirect('home')


def cross_of(request,list_id):
    list = List.objects.get(pk=list_id)
    list.completed = True
    list.save()
    return redirect('home')

def uncross(request,list_id):
    list = List.objects.get(pk=list_id)
    list.completed = False
    list.save()
    return redirect('home')
