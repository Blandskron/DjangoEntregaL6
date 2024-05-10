from django.shortcuts import render, redirect
from .forms import AutorForm


def index(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            form = AutorForm()
    return render(request, 'blog/index.html', {'form': form})

def crear_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articulos_list')
    else:
        form = AutorForm()
    return render(request, 'blog/index.html', {'form': form})
