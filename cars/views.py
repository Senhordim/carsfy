from django.views.generic import ListView, CreateView
from cars.models import Car
from cars.forms import CarModelForm

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

class CarsCreateView(CreateView):
    model = Car
    template_name = 'new.html'
    form_class = CarModelForm
    success_url = '/'



