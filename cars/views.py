from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarForm

def index(request):
  cars = Car.objects.all().order_by('created_at')
  search = request.GET.get('search')
  if search:
    cars = Car.objects.filter(model__icontains=search)
  return render(request, 'index.html', context={'cars': cars})

def new(request):
  if request.method == 'POST':
    new_car_form = CarForm(request.POST, request.FILES)
    if new_car_form.is_valid():
      new_car_form.save()
      return redirect('index')
  if request.method == 'GET':
    new_car_form = CarForm()
  return render(request, 'new.html', context={'new_car_form': new_car_form})




