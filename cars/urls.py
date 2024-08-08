from django.urls import path
from cars.views import (
  CarsCreateView,
  CarsDetailsView,
  CarsListView,
  CarsUpdateView,
  deleteCar
)

urlpatterns = [
  path('', CarsListView.as_view(), name="index"),
  path('new/', CarsCreateView.as_view(), name="new"),
  path('<int:pk>/show', CarsDetailsView.as_view(), name="show"),
  path('<int:pk>/update', CarsUpdateView.as_view(), name="update"),
  path('<int:pk>/delete', deleteCar, name="delete"),
]
