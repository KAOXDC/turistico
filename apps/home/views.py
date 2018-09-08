from django.shortcuts import render, redirect 
from .forms import *
# Create your views here.

def inicio_view(request):
	return render(request, 'home/index.html',locals())

def lugar_agregar_view(request):
	if request.method=='GET':
		form = lugar_agregar_form()
	if request.method=='POST':
		form = lugar_agregar_form(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('/lugar_listar/')

	return render(request, 'home/lugar_agregar.html',locals())

def lugar_listar_view(request):
	lista = Lugar.objects.filter()
	return render(request, 'home/lugar_listar.html',locals())

def lugar_ver_view(request, pk):
	objeto = Lugar.objects.get(id=pk)
	return render(request, 'home/lugar_ver.html',locals())

def lugar_editar_view(request, pk):
	objeto = Lugar.objects.get(id=pk)
	if request.method=='GET':
		form = lugar_agregar_form(instance=objeto)
	if request.method=='POST':
		form = lugar_agregar_form(request.POST, request.FILES, instance=objeto)
		if form.is_valid():
			form.save()
			return redirect('/lugar_listar/')
	return render(request, 'home/lugar_editar.html',locals())

def lugar_eliminar_view(request, pk):
	objeto = Lugar.objects.get(id=pk)
	if request.method=='GET':
		return render(request, 'home/lugar_eliminar.html',locals())
	if request.method=='POST':
		objeto.delete()
		return redirect('/lugar_listar/')
	return render(request, 'home/lugar_eliminar.html',locals())

def lugar_agregar_view(request):
	if request.method=='GET':
		form = lugar_agregar_form()
	if request.method=='POST':
		form = lugar_agregar_form(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('/lugar_listar/')

	return render(request, 'home/lugar_agregar.html',locals())

#xxxxxxxxxxxxxxxxxxxx     GALERIA     xxxxxxxxxxxxxxxxxxxxxxxxx

def galeria_agregar_view(request):
	if request.method=='GET':
		form = galeria_agregar_form()
	if request.method=='POST':
		form = galeria_agregar_form(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('/galeria_listar/')

	return render(request, 'home/galeria_agregar.html',locals())
def galeria_listar_view(request):
	lista = Galeria.objects.filter()
	return render(request, 'home/galeria_listar.html',locals())

def galeria_ver_view(request, pk):
	objeto = Galeria.objects.get(id=pk)
	return render(request, 'home/galeria_ver.html',locals())

def galeria_editar_view(request, pk):
	objeto = Galeria.objects.get(id=pk)
	if request.method=='GET':
		form = galeria_agregar_form(instance=objeto)
	if request.method=='POST':
		form = galeria_agregar_form(request.POST, request.FILES, instance=objeto)
		if form.is_valid():
			form.save()
			return redirect('/galeria_listar/')
	return render(request, 'home/galeria_editar.html',locals())

def galeria_eliminar_view(request, pk):
	objeto = Galeria.objects.get(id=pk)
	if request.method=='GET':
		return render(request, 'home/galeria_eliminar.html',locals())
	if request.method=='POST':
		objeto.delete()
		return redirect('/galeria_listar/')
	return render(request, 'home/galeria_eliminar.html',locals())
