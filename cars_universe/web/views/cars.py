from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib.auth import mixins as auth_mixin

from cars_universe.forms import CreateCarForm, EditCarForm, DeleteCarForm, CreateEventForm, EditEventForm, \
    DeleteEventForm
from django.views import generic as views, View

from cars_universe.web.models.additive_models import Event, Like
from cars_universe.web.models.models import Car


class CreateCarView(auth_mixin.LoginRequiredMixin, views.CreateView):

    template_name = 'car_create.html'
    form_class = CreateCarForm
    success_url = reverse_lazy('dashboard')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


def edit_car(request, pk):
    if request.user.is_authenticated:
        instance = Car.objects.get(pk=pk)
        if request.method == 'POST':
            form = EditCarForm(request.POST, instance=instance)
            if form.is_valid():
                form.save()
                return redirect('cars')
        else:
            form = EditCarForm(instance=instance)

        context = {
            'form': form,
            'car': instance,
        }
        return render(request, 'car_edit.html', context)


def delete_car(request, pk):
    if request.user.is_authenticated:
        car = Car.objects.get(pk=pk)
        if request.method == 'POST':
            form = DeleteCarForm(request.POST, instance=car)
            if form.is_valid():
                form.save()
                return redirect('cars')
        else:
            form = DeleteCarForm(instance=car)
        context = {
            'form': form,
            'car': car,
        }
        return render(request, 'car_delete.html', context)


def event_likes_count(event):
    event.likes = event.like_set.count()
    return event


@login_required
def like_event(request, pk):
    user_liked_event = Like.objects.filter(event_id=pk, user_id=request.user.pk)
    event = Event.objects.get(pk=pk)
    if user_liked_event:
        event.likes -= 1
        user_liked_event.delete()
    else:
        Like.objects.create(
            event_id=pk,
            user_id=request.user.pk,
        )
        event.likes += 1

    return redirect('event details', pk)


def event_is_liked_by_user(request, event):
    liked = Like.objects.filter(event_id=event.pk, user_id=request.user.pk)

    event.liked_by_user = True if liked else False

    return event



def create_event(request):
    if request.user.is_staff:
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


def edit_event(request, pk):
    if request.user.is_staff:
        instance = Event.objects.get(pk=pk)
        if request.method == 'POST':
            form = EditEventForm(request.POST, instance=instance)
            if form.is_valid():
                form.save()
                return redirect('dashboard')
        else:
            form = EditEventForm(instance=instance)

        context = {
            'form': form,
            'event': instance,
        }
        return render(request, 'event_edit.html', context)
    return redirect('error-500.html')


def delete_event(request, pk):
    if request.user.is_staff:
        event = Event.objects.get(pk=pk)
        if request.method == 'POST':
            form = DeleteEventForm(request.POST, instance=event)
            if form.is_valid():
                form.save()
                return redirect('events')
        else:
            form = DeleteEventForm(instance=event)
        context = {
            'form': form,
            'event': event,
        }
        return render(request, 'event_delete.html', context)
