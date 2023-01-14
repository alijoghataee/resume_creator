from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import CustomUser


class SingUpTest(TestCase):

    def test_signup_page_by_url(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)

    def test_signup_page_by_name(self):
        response = self.client.post(reverse('signup'))

    def test_signup(self):
        response = self.client.post(reverse('signup'), data={
            'username': 'testuser',
            'email': 'test@email.com',
            'password1': 'testpassword',
            'password2': 'testpassword'
        })

        self.assertEqual(response.status_code, 302)

        users = get_user_model().objects.all()
        self.assertEqual(users.count(), 1)
