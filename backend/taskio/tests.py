from django.test import TestCase
from taskio.models import Task
from taskio.serializers import TaskSerializer
from user.models import User


class TaskSerializerTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='password',
            first_name='Test',
            last_name='User',
        )
        self.task = Task.objects.create(
            title='Sample Task',
            description='A test task',
            status=Task.Status.PENDING,
            owner=self.user,
        )

    def test_serializer_contains_expected_fields(self):
        serializer = TaskSerializer(self.task)
        self.assertEqual(
            set(serializer.data.keys()),
            {'id', 'title', 'description', 'status', 'created_at', 'updated_at', 'owner'},
        )

    def test_owner_is_nested_user_info(self):
        serializer = TaskSerializer(self.task)
        owner_data = serializer.data['owner']
        self.assertIn('id', owner_data)
        self.assertIn('email', owner_data)
        self.assertNotIn('password', owner_data)

    def test_valid_status_values(self):
        for status_value in [Task.Status.PENDING, Task.Status.IN_PROGRESS, Task.Status.COMPLETED]:
            data = {'title': 'Task', 'status': status_value}
            serializer = TaskSerializer(data=data)
            serializer.is_valid()
            self.assertNotIn('status', serializer.errors)

    def test_invalid_status_raises_error(self):
        data = {'title': 'Task', 'status': 'invalid_status'}
        serializer = TaskSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('status', serializer.errors)

    def test_serializer_read_only_fields(self):
        serializer = TaskSerializer(self.task)
        self.assertIn('id', serializer.data)
        self.assertIn('created_at', serializer.data)
        self.assertIn('updated_at', serializer.data)
