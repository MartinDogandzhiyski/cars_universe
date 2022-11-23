from django import forms

from cars_universe.accounts.models import Profile
from cars_universe.helpers import BootstrapFormMixin, DisabledFieldsFormMixin
from cars_universe.web.models.additive_models import Car, Event


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
        fields = ('name', 'type', 'made_date', 'picture')
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


class CreateEventForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    photo = forms.FileField(required=False)

    class Meta:
        model = Event
        fields = ('name', 'cars_brand', 'photo', 'description', 'address', 'date')
        labels = {
            'name': 'Name',
            'cars_brand': 'Cars Brand',
            'picture': 'Event photo',
            'address': 'Address',
            'date': 'Date',
        }


class EditEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'


class DeleteEventForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Car
        fields = ('name',)




