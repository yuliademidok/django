from django.test import SimpleTestCase
from django.urls import reverse, resolve

from ..views import Login, Logout, SignUp, ProfileView, UpdateProfileView, ChangePasswordView


class TestUrls(SimpleTestCase):
    def test_login_url_resolves(self):
        url = reverse('accounts:login')
        self.assertEqual(resolve(url).func.view_class, Login)

