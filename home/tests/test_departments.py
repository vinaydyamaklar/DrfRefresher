from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from django.urls import reverse
from home.models import Department

class DepartmentAPITest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='pass1234')
        response = self.client.post(reverse('token_obtain_pair'), {
            'username': 'testuser',
            'password': 'pass1234'
        })
        self.token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

    def test_create_department(self):
        url = reverse('department-list-create')
        data = {'name': 'HR'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_department_list(self):
        Department.objects.create(name='Marketing')
        response = self.client.get(reverse('department-list-create'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_department(self):
        dept = Department.objects.create(name='Sales')
        url = reverse('department-detail', args=[dept.id])
        response = self.client.put(url, {'name': 'Global Sales'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_department(self):
        dept = Department.objects.create(name='Support')
        url = reverse('department-detail', args=[dept.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_unauthenticated_department_access(self):
        self.client.credentials()  # remove auth
        response = self.client.get(reverse('department-list-create'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
