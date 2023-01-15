from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from tasks.models import Task
import uuid
import json

class TasksTests(APITestCase):
    def test_create_task(self):
        """
        Ensure we can create a new task object.
        """
        url = reverse('task-list')
        data = {
            'title': 'task1',
            'description': '1234 bla'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.get().title, 'task1')
        self.assertEqual(Task.objects.get().description, '1234 bla')
    
    def test_retrieve_task(self):
        """
        Ensure we can retrieve a task object with uuid.
        """
        task_uuid = uuid.uuid4()
        expected_data = {
            'id':str(task_uuid),
            'title': 'task1',
            'description': '1234 bla',
            'completed': False
        }
        Task.objects.create(id=task_uuid, title='task1', description='1234 bla', completed=False)
        url = reverse('task-detail', kwargs={'pk': task_uuid})
        response = self.client.get(url)
        self.assertEqual(json.loads(response.content), expected_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
