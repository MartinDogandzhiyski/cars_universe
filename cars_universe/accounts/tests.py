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


class CreateWorkoutTests(TestCreatingAndLoggingUser):
    def test_create_workout__when_creates_new_entity__expect_workout_to_have_correct_user(self):
        user1 = self.check_if_user_is_created_and_logged_properly()
        self.client.logout()
        user2 = self.check_if_user_is_created_and_logged_properly({
            'username': 'martind19',
            'email': 'martind19@abv.bg',
            'password': 'martinch0D19',
        })






class ProfileDetailsViewTests(django_test.TestCase):
    def test_correct_template(self):
        pass

    #def test_when