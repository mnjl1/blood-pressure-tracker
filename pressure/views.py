from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import BloodPressure
from .utils import average_pressure, last_month_year


class BloodPressureListView(LoginRequiredMixin, generic.ListView):
    paginate_by = 10
    model = BloodPressure
    template_name = 'pressure/pressure_list.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        user_list = BloodPressure.objects.filter(user=self.request.user)
        systolic_pressure_list = [p.systolic_pressure for p in user_list]
        diastolic_pressure_list = [p.diastolic_pressure for p in user_list]
        date_year_set = {p.year_when_created  for p in user_list}
        date_month_set =  {p.month_when_created  for p in user_list}
        context['average_systolic_pressure'] = average_pressure(systolic_pressure_list)
        context['average_diastolic_pressure'] = average_pressure(diastolic_pressure_list)
        context['date_year_set'] = date_year_set
        context['date_month_set'] = date_month_set
        return context

    def post(self, request, *args, **kwargs):
        if 'month' in self.request.POST:
            request.session['month'] = self.request.POST.get('month')
        if 'year' in self.request.POST:
            request.session['year'] = self.request.POST.get('year')
        return HttpResponseRedirect('/pressure/')
        

    def get_queryset(self):
        user = self.request.user
        last_entry = last_month_year(user)
        default_year = last_entry[0]
        default_month = last_entry[1]
        month = self.request.session.get('month', default_month)
        year = self.request.session.get('year', default_year)
        return BloodPressure.objects.filter(user=user, created__year=year, created__month=month)
    


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
