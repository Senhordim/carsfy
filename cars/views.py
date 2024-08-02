from django.shortcuts import render

from cars.models import Car

def index(request):
  cars = Car.objects.all().order_by('created_at')
  search = request.GET.get('search')
  if search:
    cars = Car.objects.filter(model__icontains=search)
  return render(request, 'index.html', context={'cars': cars})
