from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import BloodPressure
from .utils import average_pressure


class BloodPressureListView(LoginRequiredMixin, generic.ListView):
    paginate_by = 10
    model = BloodPressure
    template_name = 'pressure/pressure_list.html'

    def get_queryset(self):
        return BloodPressure.objects.filter(user=self.request.user)
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        user_list = BloodPressure.objects.filter(user=self.request.user)
        systolic_pressure_list = [p.systolic_pressure for p in user_list]
        diastolic_pressure_list = [p.diastolic_pressure for p in user_list]
        context['average_systolic_pressure'] = average_pressure(systolic_pressure_list)
        context['average_diastolic_pressure'] = average_pressure(diastolic_pressure_list)
        return context


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
