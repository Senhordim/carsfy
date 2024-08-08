from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView
  )
from django.urls import reverse_lazy
from django.shortcuts import redirect
from cars.models import Car
from cars.forms import CarModelForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
class CarsListView(ListView):
    model = Car
    template_name = 'index.html'
    context_object_name = 'cars'

    def get_queryset(self):
        cars = super().get_queryset().order_by('-created_at')
        search = self.request.GET.get('search')
        if search:
            cars = Car.objects.filter(model__icontains=search)
        return cars

@method_decorator(login_required(login_url="auth"), name='dispatch')
class CarsCreateView(CreateView):
    model = Car
    template_name = 'new.html'
    form_class = CarModelForm
    success_url = '/'

class CarsDetailsView(DetailView):
    model = Car
    template_name = 'show.html'

@method_decorator(login_required(login_url="auth"), name='dispatch')
class CarsUpdateView(UpdateView):
    model = Car
    template_name = 'edit.html'
    form_class = CarModelForm

    def get_success_url(self):
        return reverse_lazy('show', kwargs={'pk': self.object.pk})


def deleteCar(request, pk):
    car = Car.objects.get(pk=pk)
    car.delete()
    return redirect('/')



