from django.urls import path

from cars_universe.web.views.cars import create_event, delete_event, edit_event, CreateCarView, EditCarView, \
    DeleteCarView
from cars_universe.web.views.generic import HomeView, DashboardView, EventDetailsView, ShowEventsView, ShowCarsView, \
    ShowToolsView, ToolDetailsView
from cars_universe.web.views.tools import create_tool, delete_tool, edit_tool

urlpatterns = (
    path('', HomeView.as_view(), name='home_pg'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('event/create/', create_event, name='event create'),
    path('event/edit/<int:pk>/', edit_event, name='edit event'),
    path('event/delete/<int:pk>/', delete_event, name='delete event'),
    path('events/', ShowEventsView.as_view(), name='events'),
    path('event/details/<int:pk>/', EventDetailsView.as_view(), name='event details'),
    path('car/create/', CreateCarView.as_view(), name='create car'),
    path('cars', ShowCarsView.as_view(), name='cars'),
    path('car/edit/<int:pk>/', EditCarView.as_view(), name='edit car'),
    path('car/delete/<int:pk>/', DeleteCarView.as_view(), name='delete car'),
    path('tool/create/', create_tool, name='tool create'),
    path('tool/edit/<int:pk>/', edit_tool, name='edit tool'),
    path('tool/delete/<int:pk>/', delete_tool, name='delete tool'),
    path('tools/', ShowToolsView.as_view(), name='tools'),
    path('tool/details/<int:pk>/', ToolDetailsView.as_view(), name='tool details'),

)