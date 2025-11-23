from django.test import TestCase
from django.urls import reverse
from .models import TodoItem

class TodoItemModelTest(TestCase):
    def test_create_todo(self):
        todo = TodoItem.objects.create(title="Test Todo")
        self.assertEqual(str(todo), "Test Todo")
        self.assertFalse(todo.is_resolved)

class TodoViewTest(TestCase):
    def setUp(self):
        self.todo = TodoItem.objects.create(title="Test Todo")

    def test_todo_list_view(self):
        response = self.client.get(reverse('todo-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Todo")

    def test_todo_create_view(self):
        response = self.client.post(reverse('todo-add'), {
            'title': 'New Todo',
            'description': 'New Description'
        })
        self.assertEqual(response.status_code, 302) # Redirects after success
        self.assertEqual(TodoItem.objects.count(), 2)

    def test_todo_resolve(self):
        response = self.client.get(reverse('todo-toggle-resolved', args=[self.todo.pk]))
        self.assertEqual(response.status_code, 302)
        self.todo.refresh_from_db()
        self.assertTrue(self.todo.is_resolved)
