from pyexpat import model
from urllib import request
from django.views import generic

from .models import BloodPressure


class BloodPressureListView(generic.ListView):
    model = BloodPressure
    context_object_name = 'pressure_list'
    template_name = 'pressure/pressure_list.html'

    def get_queryset(self):
        return BloodPressure.objects.filter(user=self.request.user)


class BloodPressureDetailView(generic.DetailView):
    model = BloodPressure
