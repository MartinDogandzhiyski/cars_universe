from django.views import generic as views
from django.shortcuts import render, redirect

from cars_universe.common.views_mixins import RedirectToDashboard
from cars_universe.web.models import CarPhoto


class HomeView(views.TemplateView):
    template_name = 'home-no-profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hide_additional_nav_items'] = False
        return context


class DashboardView(views.ListView):
    model = CarPhoto
    template_name = 'dashboard.html'


#class DashboardView(views.ListView):
  #  model = CarPhoto
   # template_name = 'main/dashboard.html'
    #context_object_name = 'car_photos'