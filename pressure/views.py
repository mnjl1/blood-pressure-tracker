from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import BloodPressure


class BloodPressureListView(LoginRequiredMixin ,generic.ListView):
    model = BloodPressure
    context_object_name = 'pressure_list'
    template_name = 'pressure/pressure_list.html'

    def get_queryset(self):
        return BloodPressure.objects.filter(user=self.request.user)


class BloodPressureDetailView(generic.DetailView):
    model = BloodPressure
