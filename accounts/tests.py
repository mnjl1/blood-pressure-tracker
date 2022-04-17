from django.test import TestCase
from django.contrib.auth import get_user_model

class UserManagersTests(TestCase):

    def test_create_uses(self):
        User = get_user_model()
        user = User.objects.create_user(email='user@email.com', password='testpass')
        self.assertEqual(user.email, 'user@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.asertFalse(user.is_superuser)
        try:
            self.assertIsNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email='')
        with self.assertRaises(ValueError):
            User.objects.create_user(email='', password="testpass")

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(email='admin@email.com', password='testpass')
        self.assertEqual(admin_user.email, 'admin@email.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        try:
            self.assertIsNone(admin_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email='admin@email.com', password='testpass', is_superuser=False)
