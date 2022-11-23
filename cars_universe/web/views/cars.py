from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib.auth import mixins as auth_mixin

from cars_universe.forms import CreateCarForm, EditCarForm, DeleteCarForm, CreateEventForm
from django.views import generic as views


class CreateCarView(auth_mixin.LoginRequiredMixin, views.CreateView):
    template_name = 'car_create.html'
    form_class = CreateCarForm
    success_url = reverse_lazy('dashboard')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


def create_event(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CreateEventForm(request.POST, request.FILES)

            if form.is_valid():
                form.save()
                return redirect('dashboard')
        else:
            form = CreateEventForm()
        context = {
            'form': form,
        }
        return render(request, 'event_create.html', context)


class EditCarView(auth_mixin.LoginRequiredMixin, views.UpdateView):
    template_name = 'main/car_edit.html'
    form_class = EditCarForm


class DeleteCarView(auth_mixin.LoginRequiredMixin, views.DeleteView):
    template_name = 'main/car_delete.html'
    form_class = DeleteCarForm