from django.urls import path
from . import views
from cars_universe.web.views.car_parts import create_part, delete_part, edit_part, add_to_cart, cart_page, \
    remove_from_cart, clear_cart, view_orders, place_order
from cars_universe.web.views.cars import create_event, delete_event, edit_event, CreateCarView, edit_car, delete_car, \
    like_event, like_car

from cars_universe.web.views.generic import HomeView, DashboardView, EventDetailsView, ShowEventsView, ShowCarsView, \
    ShowToolsView, ToolDetailsView, about, PartDetailsView, ShowPartsView, CarDetailsView, add_comment
from cars_universe.web.views.tools import create_tool, delete_tool, edit_tool

urlpatterns = (
    path('', HomeView.as_view(), name='home_pg'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('event/create/', create_event, name='event create'),
    path('event/edit/<int:pk>/', edit_event, name='edit event'),
    path('event/delete/<int:pk>/', delete_event, name='delete event'),
    path('events/', ShowEventsView.as_view(), name='events'),
    path('event/details/<int:pk>/', EventDetailsView.as_view(), name='event details'),
    path('like/<int:pk>/', like_event, name='like eventt'),
    path('like/car/<int:pk>/', like_car, name='like car'),
    path('car/create/', CreateCarView.as_view(), name='create car'),
    path('cars', ShowCarsView.as_view(), name='cars'),
    path('car/details/<int:pk>/', CarDetailsView.as_view(), name='car details'),
    path('car/edit/<int:pk>/', edit_car, name='edit car'),
    path('car/delete/<int:pk>/', delete_car, name='delete car'),
    path('tool/create/', create_tool, name='tool create'),
    path('tool/edit/<int:pk>/', edit_tool, name='edit tool'),
    path('tool/delete/<int:pk>/', delete_tool, name='delete tool'),
    path('tools/', ShowToolsView.as_view(), name='tools'),
    path('tool/details/<int:pk>/', ToolDetailsView.as_view(), name='tool details'),
    path('part/create/', create_part, name='part create'),
    path('part/edit/<int:pk>/', edit_part, name='edit part'),
    path('part/delete/<int:pk>/', delete_part, name='delete part'),
    path('parts/', ShowPartsView.as_view(), name='parts'),
    path('part/details/<int:pk>/', PartDetailsView.as_view(), name='part details'),
    path('about/', about, name='about'),
    path('event/details/<int:event_id>/add_comment/', add_comment, name='add_comment'),
    path('add-to-cart/<int:item_id>/<str:item_type>/', add_to_cart, name='add_to_cart'),
    path('cart/', cart_page, name='cart'),
    path('cart/remove/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
    path('cart/clear/', clear_cart, name='clear_cart'),
    path('orders/', view_orders, name='view_orders'),
    path('place_order/', place_order, name='place_order'),

)
