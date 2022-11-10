from django.urls import path, reverse_lazy
from django.views.generic import RedirectView

from cars_universe.accounts.views import UserRegisterView, UserLoginView

urlpatterns = (
    path('create/', UserRegisterView.as_view(), name='create profile'),
    path('login/', UserLoginView.as_view(), name='login user'),
)
