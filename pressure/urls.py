from unicodedata import name
from django.urls import path

from .views import BloodPressureListView, BloodPressureCreateView


urlpatterns = [
    path('', BloodPressureListView.as_view(), name='pressure_list'),
    path('add/', BloodPressureCreateView.as_view(), name='pressure_create'),
]