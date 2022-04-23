
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class BloodPressure(models.Model):
    # TODO implement uuid
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,)
    systolic_pressure = models.IntegerField(blank=False)
    diastolic_pressure = models.IntegerField(blank=False)
    heart_rate = models.IntegerField(blank=True)
    last_modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)
    
    def __str__(self):
        return f'{self.user}, {self.systolic_pressure}, {self.diastolic_pressure}, {self.heart_rate}'
    
    def get_absolute_url(self): # new
        return reverse('pressure_detail', args=[str(self.id)])