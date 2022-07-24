from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from accounts_app.models import User
from ..serializers.publications import PostSerializer
from ...models import Post


class PostsApiTest(APITestCase):

    def setUp(self):
        user = User.objects.create(username="Test User 1")
        self.post_1 = Post.objects.create(title="Test post 1", user=user)
        self.post_2 = Post.objects.create(title="Test post 1", user=user)

    def test_get(self):
        url = reverse('post-list')
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

        serializer_data = PostSerializer([self.post_2, self.post_1], many=True).data
        self.assertEqual(serializer_data, response.data['results'])



