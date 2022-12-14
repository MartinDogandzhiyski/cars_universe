from django import test as django_test
from django.contrib.auth import get_user_model
UserModel = get_user_model()


class TestCreatingAndLoggingUser(django_test.TestCase):
    CREDENTIALS = {
        'username': 'martinD',
        'email': 'martto56@abv.bg',
        'password': '147258md',
    }

    def check_if_user_is_created_and_logged_properly(self, credentials=None):
        if credentials is None:
            credentials = self.CREDENTIALS
        user = UserModel.objects.create_user(**credentials)
        self.client.login(**credentials)
        return user







class ProfileDetailsViewTests(django_test.TestCase):
    def test_correct_template(self):
        pass

    #def test_when