from django.test import TestCase
from django.urls import reverse
from accounts.models import CustomUser
from .models import BloodPressure


class BloodPressureTest(TestCase):
    
    def setUp(self):
        self.user = CustomUser.objects.create(
            email='e@e.com',
            password='123'
        )

        self.pressure = BloodPressure.objects.create(
            user=self.user,
            systolic_pressure=120,
            diastolic_pressure=80,
            heart_rate=60
        )
    
    def test_blood_pressure_created(self):
        self.assertEqual(self.pressure.systolic_pressure, 120)
        self.assertEqual(self.pressure.diastolic_pressure, 80)
        self.assertEqual(self.pressure.heart_rate, 60)
        self.assertEqual(self.user.email, 'e@e.com')
    
    def test_pressure_list_view(self):
        self.client.login(email='e@e.com', password='123')
        response = self.client.get(reverse('pressure_list'))
        self.assertEqual(response.status_code, 200)
    


