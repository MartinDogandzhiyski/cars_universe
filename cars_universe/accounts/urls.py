from django.urls import path, reverse_lazy
from django.views.generic import RedirectView

from cars_universe.accounts.views import UserRegisterView, UserLoginView, ProfileDetailsView, ChangeUserPasswordView

urlpatterns = (
    path('create/', UserRegisterView.as_view(), name='create profile'),
    path('login/', UserLoginView.as_view(), name='login user'),
path('edit-password/', ChangeUserPasswordView.as_view(), name='change password'),
    path('password-change_done/', RedirectView.as_view(url=reverse_lazy('dashboard')), name='password-change_done'),
    path('details/<int:pk>/', ProfileDetailsView.as_view(), name='profile details'),
)
