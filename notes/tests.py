from django.test import TestCase

# Create your tests here.
# notes/tests.py
from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status
from .models import Note

class NotesSearchPaginationTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='tester', password='pass123')
        # create sample notes
        for i in range(12):
            Note.objects.create(owner=self.user, title=f"Note {i}", content="sample content")

        # login to get token if using JWT; or use force_authenticate in tests
        self.client.force_authenticate(user=self.user)

    def test_pagination(self):
        url = reverse('note-list')  # DefaultRouter name: 'note-list'
        resp = self.client.get(url)
        # default PAGE_SIZE = 5, so first page should contain 5 results
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertTrue('results' in resp.data)
        self.assertEqual(len(resp.data['results']), 5)

    def test_search(self):
        url = reverse('note-list') + '?search=Note 1'
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        # At least one result containing "Note 1"
        self.assertTrue(any('Note 1' in item['title'] for item in resp.data['results']))