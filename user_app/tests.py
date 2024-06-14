from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
class RegisterTest(APITestCase):
    def test_register(self):
        url = reverse('registration-views')
        data = {
            'username':'Test',
            'email':'test@test.com',
            'password':'test123',
            'password2':'test123'
        }
        response = self.client.post(url,data,format='json')
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
class LoginTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='Test',password='test123')
    def test_loginlogout(self):
        url = reverse('login')
        data = {
            'username':'Test',
            'password':'test123'
        }
        response = self.client.post(url,data,type='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
    def test_logout(self):
        self.token = Token.objects.get(user__username = "Test")
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        url = reverse('logout_views')
        response = self.client.post(url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        