from django.urls import path

from cars_universe.web.views.cars import CreateEventView
from cars_universe.web.views.generic import HomeView, DashboardView

urlpatterns = (
    path('', HomeView.as_view(), name='home_pg'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('event/create/', CreateEventView.as_view(), name='event create'),


)