from django import forms

from cars_universe.accounts.models import Profile
from cars_universe.helpers import BootstrapFormMixin, DisabledFieldsFormMixin
from cars_universe.web.models.additive_models import Car, Event, Comment
from cars_universe.web.models.models import Tool, CarPart


class OrderForm(forms.Form):
    address = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Enter your address'}))


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
        fields = ('name', 'type', 'hp', 'made_date', 'photo')
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter car project name',

                }
            )
        }


class EditCarForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Car
        fields = ('name', 'type', 'hp', 'made_date', 'photo')


class DeleteCarForm(forms.ModelForm):
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
        fields = ('name', 'cars_brand', 'photo', 'description', 'address', 'date')
        labels = {
            'name': 'Name',
            'cars_brand': 'Cars Brand',
            'picture': 'Event photo',
            'address': 'Address',
            'date': 'Date',
        }


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


class CreateToolForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    photo = forms.FileField(required=False)

    class Meta:
        model = Tool
        fields = ('name', 'type', 'brand', 'photo', 'description', 'price')
        labels = {
            'name': 'Name',
            'type': 'Type',
            'brand': 'Brand',
            'description': 'Description',
            'photo': 'Tool photo',
            'price': 'Price'

        }


class EditToolForm(forms.ModelForm):
    class Meta:
        model = Tool
        fields = '__all__'


class DeleteToolForm(forms.ModelForm):
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


class CreatePartForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    photo = forms.FileField(required=False)

    class Meta:
        model = CarPart
        fields = ('name', 'type', 'brand', 'brand_for', 'photo', 'description', 'price')
        labels = {
            'name': 'Name',
            'type': 'Type',
            'brand': 'Brand',
            'brand_for': 'Brand For',
            'description': 'Description',
            'photo': 'Part photo',
            'price': 'Price'

        }


class EditPartForm(forms.ModelForm):
    class Meta:
        model = CarPart
        fields = '__all__'


class DeletePartForm(forms.ModelForm):
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


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
