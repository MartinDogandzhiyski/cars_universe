from django.urls import reverse_lazy

from cars_universe.forms import CreateCarForm, EditCarForm, DeleteCarForm, CreateEventForm
from django.views import generic as views


class CreateCarView(views.CreateView):
    template_name = 'main/car_create.html'
    form_class = CreateCarForm
    success_url = reverse_lazy('dashboard')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class CreateEventView(views.CreateView):
    template_name = 'event_create.html'
    form_class = CreateEventForm
    success_url = reverse_lazy('dashboard')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs



class EditCarView(views.UpdateView):
    template_name = 'main/car_edit.html'
    form_class = EditCarForm


class DeleteCarView(views.DeleteView):
    template_name = 'main/car_delete.html'
    form_class = DeleteCarForm