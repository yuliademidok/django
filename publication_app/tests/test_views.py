from django.test import Client, TransactionTestCase
from django.urls import reverse

import json

from accounts_app.models import User
from ..models import Post


class TestView(TransactionTestCase):

    def setUp(self):
        self.client = Client()
        self.credentials = {"username": "test", "password": "testpass1"}
        self.user = User.objects.create_user(**self.credentials)
        self.client.login(**self.credentials)

        self.post_1 = Post.objects.create(title="Post test 1", text="Text post 1", user=self.user)

        self.main_page = reverse("publication:main_page")
        self.post_detail = reverse("publication:post_detail", args=[self.post_1.id])
        self.add_post = reverse("publication:add_post")

    def test_posts_list_GET(self):
        response = self.client.get(self.main_page)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "publication_app/mainpage.html")

    def test_post_detail_GET(self):
        response = self.client.get(self.post_detail)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "publication_app/post_detail.html")

    def test_post_POST(self):
        response = self.client.post(self.add_post, {"title": "Post test 2", "text": "Text post 2"})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.user.posts.first().title, "Post test 2")
        self.assertEqual(self.user.posts.first().text, "Text post 2")

    def test_post_no_data_added_POST(self):
        posts_count_before = Post.objects.count()
        response = self.client.post(self.add_post, {})
        posts_count_after = Post.objects.count()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(posts_count_before, posts_count_after)

    # def test_post_DELETE(self):
    #     response = self.client.delete(self.post_detail, json.dumps({"id": self.post_1.id}))
