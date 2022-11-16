from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model
from cars_universe.accounts.models import Profile
from cars_universe.helpers import BootstrapFormMixin
from cars_universe.web.models.models import CarPhoto


class CreateProfileForm(BootstrapFormMixin, auth_forms.UserCreationForm):
    first_name = forms.CharField(
        max_length=Profile.FIRST_NAME_MAX_LENGTH,
    )
    last_name = forms.CharField(
        max_length=Profile.LAST_NAME_MAX_LENGTH,
    )
    picture = forms.URLField(

    )
    date_of_birth = forms.DateField(

    )
    description = forms.CharField(
        widget=forms.Textarea,
    )
    email = forms.EmailField(

    )
    gender = forms.ChoiceField(
        choices=Profile.Genders,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        user = super().save(commit=commit)

        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            picture=self.cleaned_data['picture'],
            date_of_birth=self.cleaned_data['date_of_birth'],
            description=self.cleaned_data['description'],
            email=self.cleaned_data['email'],
            gender=self.cleaned_data['gender'],

            user=user,
        )
        if commit:
            profile.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'picture', 'description')
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter first name',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter last name',
                }
            ),
            'picture': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter URL',
                }
            ),
        }

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter first name',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter last name',
                }
            ),
            'picture': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter URL',
                }
            ),
            'date_of_birth': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'min': '1920-01-01'
                }
            ),

            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter email',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter description',
                    'rows': 3
                }
            ),

        }


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        CarPhoto.objects.all().delete()
        self.instance.delete()
        return self.instance

    class Meta:
        model = Profile
        fields = ()