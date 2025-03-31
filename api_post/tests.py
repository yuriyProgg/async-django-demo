from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.http import HttpResponse


class PostAPITest(APITestCase):
    def setUp(self):
        response = self.client.post(
            reverse("api posts"),
            {"title": "test", "content": "test"},
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.post = response.data

    def test_post_creation(self):
        self.assertEqual(self.post.get("title"), "test")
        self.assertEqual(self.post.get("content"), "test")

    def test_delete(self):
        response: HttpResponse = self.client.delete(
            reverse("api post destroy", args=[self.post.get("id")]),
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
