from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from rest_framework import status

User = get_user_model()


class UserProfileUpdateViewTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='TestPass123!',
            first_name='John',
            last_name='Doe',
        )
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_patch_update_first_name(self):
        response = self.client.patch('/user/profile/', {'first_name': 'Jane'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'], 'Jane')
        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, 'Jane')

    def test_patch_update_last_name(self):
        response = self.client.patch('/user/profile/', {'last_name': 'Smith'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['last_name'], 'Smith')
        self.user.refresh_from_db()
        self.assertEqual(self.user.last_name, 'Smith')

    def test_patch_update_multiple_fields(self):
        response = self.client.patch('/user/profile/', {
            'first_name': 'Jane',
            'last_name': 'Smith',
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'], 'Jane')
        self.assertEqual(response.data['last_name'], 'Smith')

    def test_patch_cannot_update_email(self):
        response = self.client.patch('/user/profile/', {'email': 'new@example.com'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertEqual(self.user.email, 'test@example.com')

    def test_patch_cannot_update_password(self):
        response = self.client.patch('/user/profile/', {'password': 'NewPass123!'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password('TestPass123!'))

    def test_unauthenticated_request(self):
        client = APIClient()
        response = client.patch('/user/profile/', {'first_name': 'Jane'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_put_update_profile(self):
        response = self.client.put('/user/profile/', {
            'first_name': 'Jane',
            'last_name': 'Smith',
            'username': 'janesmith',
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'], 'Jane')
        self.assertEqual(response.data['last_name'], 'Smith')
        self.assertEqual(response.data['username'], 'janesmith')
