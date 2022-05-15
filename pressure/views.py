from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import BloodPressure


class BloodPressureListView(LoginRequiredMixin ,generic.ListView):
    model = BloodPressure
    context_object_name = 'pressure_list'
    template_name = 'pressure/pressure_list.html'

    def get_queryset(self):
        return BloodPressure.objects.filter(user=self.request.user)


class BloodPressureCreateView(LoginRequiredMixin, generic.CreateView):
    model = BloodPressure
    fields = ['systolic_pressure', 'diastolic_pressure', 'heart_rate']
    template_name = 'pressure/pressure_create.html'
    success_url = reverse_lazy('pressure_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class BloodPressureDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = BloodPressure
    success_url = reverse_lazy('pressure_list')


# TODO Django charts or some another implementations
