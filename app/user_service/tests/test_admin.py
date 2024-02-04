"""
Tests for Django admin modifications.
"""

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import Client


class AdminSiteTests(TestCase):
    """Test for Django admin."""

    @classmethod
    def setUpTestData(cls):
        """Create user and client."""

        # create superuser and login
        cls.admin_user = get_user_model().objects.create_superuser(
            email="admin@myemail.com",
            password="mysecurepass"
        )

        # create regular user
        cls.regular_user = get_user_model().objects.create_user(
            email="anotheruser@myemail.com",
            password="anothersecurepass",
            name="Test User"
        )

    def test_users_list(self):
        """Test that users are listed on page."""
        client = Client()
        client.force_login(self.admin_user)
        url = reverse("admin:user_service_user_changelist")
        res = client.get(url, follow=True)

        self.assertContains(res, self.regular_user.name)
        self.assertContains(res, self.regular_user.email)

    def test_edit_user_page(self):
        """Test edit user page works."""
        client = Client()
        client.force_login(self.admin_user)
        url = reverse("admin:user_service_user_change",
                      args=[self.regular_user.id])
        res = self.client.get(url, follow=True)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """Test create user page works."""
        client = Client()
        client.force_login(self.admin_user)
        url = reverse("admin:user_service_user_add")
        res = self.client.get(url, follow=True)

        self.assertEqual(res.status_code, 200)
