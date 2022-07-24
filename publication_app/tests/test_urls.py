from django.test import SimpleTestCase
from django.urls import reverse, resolve

from ..views import MainView, DetailView


class TestUrls(SimpleTestCase):
    def test_main_page_url_resolves(self):
        url = reverse('publication:main_page')
        self.assertEqual(resolve(url).func.view_class, MainView)

    def test_post_detail_page_url_resolves(self):
        url = reverse('publication:post_detail', args=["1"])
        self.assertEqual(resolve(url).func.view_class, DetailView)
