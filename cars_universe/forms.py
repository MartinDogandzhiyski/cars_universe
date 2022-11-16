from django import forms

from cars_universe.accounts.models import Profile
from cars_universe.helpers import BootstrapFormMixin, DisabledFieldsFormMixin
from cars_universe.web.models import CarPhoto, Car, Event


class CreateCarForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        car = super().save(commit=False)

        car.user = self.user
        if commit:
            car.save()
        return car

    class Meta:
        model = Car
        fields = ('name', 'type', 'made_date')
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter car name',

                }
            )
        }


class EditCarForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Car
        exclude = ('user_profile',)


class DeleteCarForm(BootstrapFormMixin, DisabledFieldsFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self._init_disabled_fields()

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Car
        exclude = ('user_profile',)


class CreateCarPhotoForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    photo = forms.FileField(required=False)

    class Meta:
        model = CarPhoto
        fields = ('photo', 'description', 'tagged_cars')
        widgets = {
            'photo': forms.FileInput(
                attrs={
                    'class': 'form-control-file',

                }
            ),

            'description': forms.TextInput(
                attrs={
                    'placeholder': 'Enter description',

                }
            ),

        }


class EditCarPhotoForm(BootstrapFormMixin, DisabledFieldsFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self._init_disabled_fields()

    class Meta:
        model = CarPhoto
        fields = ('photo', 'description', 'tagged_cars')


class CreateEventForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self._init_bootstrap_form_controls()


    class Meta:
        model = Event
        fields = ('name', 'cars_brand', 'address', 'date',)
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter car name',

                }
            ),

        }


