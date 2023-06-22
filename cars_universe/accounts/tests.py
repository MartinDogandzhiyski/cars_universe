from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User
from cars_universe.accounts.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm
from cars_universe.accounts.models import Profile
from cars_universe.web.models.models import Car
from django.contrib.auth import logout
from django.contrib.auth import get_user_model
from django.contrib.auth.views import PasswordChangeView

UserModel = get_user_model()


class ViewTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.profile = Profile.objects.create(user=self.user)
        self.car = Car.objects.create(user=self.user, name='Test Car')

    def test_user_register_view(self):
        url = reverse('user_register')
        data = {
            'username': 'newuser',
            'password1': 'newpass',
            'password2': 'newpass'
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login user'))
        self.assertEqual(UserModel.objects.count(), 2)

    def test_user_login_view(self):
        url = reverse('user_login')
        data = {
            'username': 'testuser',
            'password': 'testpass'
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('dashboard'))

    def test_logout_view(self):
        url = reverse('logout')
        request = self.factory.post(url)
        request.user = self.user
        response = logout(request)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login user'))

    def test_change_user_password_view(self):
        url = reverse('change_password')
        request = self.factory.get(url)
        request.user = self.user
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/change_password.html')
        self.assertIsInstance(response.context['view'], PasswordChangeView)
        self.assertEqual(response.context['view'].success_url, reverse('password-change_done'))

    def test_profile_details_view(self):
        url = reverse('profile_details', args=[self.profile.pk])
        request = self.factory.get(url)
        request.user = self.user
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile_details.html')
        self.assertEqual(response.context['profile'], self.profile)
        self.assertEqual(len(response.context['cars']), 1)
        self.assertTrue(response.context['is_owner'])
        self.assertEqual(response.context['cars'][0], self.car)

    def test_edit_profile_view(self):
        url = reverse('edit_profile', args=[self.profile.pk])
        request = self.factory.get(url)
        request.user = self.user
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/profile_edit.html')
        self.assertIsInstance(response.context['form'], EditProfileForm)

    def test_delete_profile_view(self):
        url = reverse('delete_profile', args=[self.profile.pk])
        request = self.factory.get(url)
        request.user = self.user
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/profile_delete.html')
        self.assertIsInstance(response.context['form'], DeleteProfileForm)







