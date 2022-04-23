from django.urls import path

from .views import BloodPressureListView


urlpatterns = [
    path('', BloodPressureListView.as_view(), name='pressure_list'),
]