from django.forms.fields import EmailField
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_success(self):
        """Test creating a user with email instead of username"""
        email = "test@test.com"
        password = "Pass1234"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
    
    def test_create_user_without_email_fail(self):
        """Test creating user with only email"""
        with self.assertRaises(ValueError):
            user = get_user_model().objects.create_user(None, "Pass1234")
    

    def test_create_super_user(self):
        """Test creating and saving super user"""
        user = get_user_model().objects.create_superuser(
            email="test@test.com",
            password="Pass1234"
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
    

    def test_create_user_is_active(self):
        """Test creating user with active status"""
        user = get_user_model().objects.create_user("test@test.com", "Pass1234")

        self.assertTrue(user.is_active)
    

    def test_create_user_with_normalized_email(self):
        """Test creating user with normalized email"""
        email = "test@TEST.com"
        user = get_user_model().objects.create_user(email, "Pass1234")

        self.assertEqual(user.email, email.lower())