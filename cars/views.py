from django.shortcuts import render

from cars.models import Car

def index(request):
  # cars = Car.objects.filter(brand__name='Fiat')
  # cars = Car.objects.filter(model__contains='Uno')
  cars = Car.objects.all()
  return render(request, 'index.html', context={'cars': cars})
