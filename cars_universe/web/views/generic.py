from django.views import generic as views

from cars_universe.web.models.additive_models import Event
from cars_universe.web.models.models import CarPhoto, Car, Tool


class HomeView(views.TemplateView):
    template_name = 'home_no_profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hide_additional_nav_items'] = False
        return context


class DashboardView(views.ListView):
    model = CarPhoto
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events'] = Event.objects.all()
        context['tools'] = Tool.objects.all()
        return context


class ShowEventsView(views.ListView):
    model = Event
    template_name = 'events.html'
    context_object_name = 'events'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events'] = Event.objects.all()

        return context


class EventDetailsView(views.DetailView):
    model = Event
    template_name = 'event_details.html'
    context_object_name = 'event'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events'] = Event.objects.all()

        return context


class ShowCarsView(views.ListView):
    model = Event
    template_name = 'cars.html'
    context_object_name = 'car'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_cars'] = Car.objects.all()
        return context


class ShowToolsView(views.ListView):
    model = Tool
    template_name = 'tools.html'
    context_object_name = 'tools'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tools'] = Tool.objects.all()

        return context


class ToolDetailsView(views.DetailView):
    model = Tool
    template_name = 'tool_details.html'
    context_object_name = 'tool'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tools'] = Tool.objects.all()

        return context
