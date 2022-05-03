from django.urls import path

from .views import BloodPressureListView, BloodPressureCreateView, BloodPressureDeleteView


urlpatterns = [
    path('', BloodPressureListView.as_view(), name='pressure_list'),
    path('add/', BloodPressureCreateView.as_view(), name='pressure_create'),
    path('delete/<int:pk>/', BloodPressureDeleteView.as_view(), name='pressure_delete'),
]