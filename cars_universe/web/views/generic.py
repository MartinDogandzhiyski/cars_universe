from django.shortcuts import render
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixin
from cars_universe.accounts.models import CarsUniverseUser, Profile
from cars_universe.web.models.additive_models import Event
from cars_universe.web.models.models import Car, Tool, CarPart
from cars_universe.web.views.cars import event_is_liked_by_user, event_likes_count


def about(request):
    profiles = Profile.objects.all()

    context = {
        'profiles': profiles,
    }
    return render(request, 'about.html', context)


class HomeView(views.TemplateView):
    template_name = 'home_no_profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hide_additional_nav_items'] = False
        return context


class DashboardView(auth_mixin.LoginRequiredMixin, views.ListView):
    model = Event
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events'] = Event.objects.all()
        context['tools'] = Tool.objects.all()
        return context


class ShowEventsView(auth_mixin.LoginRequiredMixin, views.ListView):
    model = Event
    template_name = 'events.html'
    context_object_name = 'events'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events'] = Event.objects.all()

        return context


class EventDetailsView(auth_mixin.LoginRequiredMixin, views.DetailView):
    model = Event
    template_name = 'event_details.html'
    context_object_name = 'event'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        event_likes_count(self.object)
        event_is_liked_by_user(self.request, self.object)
        context['events'] = Event.objects.all()
        return context


class ShowCarsView(auth_mixin.LoginRequiredMixin, views.ListView):
    model = Event
    template_name = 'cars.html'
    context_object_name = 'car'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_cars'] = Car.objects.all()
        return context


class CarDetailsView(auth_mixin.LoginRequiredMixin, views.DetailView):
    model = Car
    template_name = 'car_details.html'
    context_object_name = 'car'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cars'] = Car.objects.all()

        return context


class ShowToolsView(auth_mixin.LoginRequiredMixin, views.ListView):
    model = Tool
    template_name = 'tools.html'
    context_object_name = 'tools'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tools'] = Tool.objects.all()

        return context


class ToolDetailsView(auth_mixin.LoginRequiredMixin, views.DetailView):
    model = Tool
    template_name = 'tool_details.html'
    context_object_name = 'tool'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tools'] = Tool.objects.all()

        return context


class ShowPartsView(auth_mixin.LoginRequiredMixin, views.ListView):
    model = CarPart
    template_name = 'parts.html'
    context_object_name = 'parts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['parts'] = CarPart.objects.all()

        return context


class PartDetailsView(auth_mixin.LoginRequiredMixin, views.DetailView):
    model = CarPart
    template_name = 'part_details.html'
    context_object_name = 'part'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['parts'] = CarPart.objects.all()

        return context




