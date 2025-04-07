from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from django.urls import reverse
from home.models import Employee, Department

class EmployeeAPITest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='pass1234')
        response = self.client.post(reverse('token_obtain_pair'), {
            'username': 'testuser',
            'password': 'pass1234'
        })
        self.token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

        self.department = Department.objects.create(name='Engineering')

    def test_create_employee(self):
        url = reverse('employee-list-create')
        data = {'name': 'Alice', 'email': 'alice@example.com', 'department': self.department.id}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_employee_list(self):
        Employee.objects.create(name='Bob', email='bob@example.com', department=self.department)
        response = self.client.get(reverse('employee-list-create'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_employee(self):
        emp = Employee.objects.create(name='Eve', email='eve@example.com', department=self.department)
        url = reverse('employee-detail', args=[emp.id])
        response = self.client.put(url, {'name': 'Eve Updated', 'email': 'eve@example.com', 'department': self.department.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_employee(self):
        emp = Employee.objects.create(name='Dan', email='dan@example.com', department=self.department)
        url = reverse('employee-detail', args=[emp.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_unauthenticated_employee_access(self):
        self.client.credentials()  # remove auth
        response = self.client.get(reverse('employee-list-create'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
