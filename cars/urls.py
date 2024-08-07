from django.urls import path
from cars.views import CarsListView, CarsCreateView

urlpatterns = [
  path('', CarsListView.as_view(), name="index"),
  path('new/', CarsCreateView.as_view(), name="new"),
]
