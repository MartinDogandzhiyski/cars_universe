from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views, logout
from django.contrib.auth import mixins as auth_mixin
from cars_universe.accounts.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm
from cars_universe.accounts.models import Profile
from django.views import generic as views
from cars_universe.common.views_mixins import RedirectToDashboard
from cars_universe.web.models.models import Car, CarPhoto


class UserRegisterView(views.CreateView):
    form_class = CreateProfileForm
    template_name = 'accounts/profile_create.html'
    success_url = reverse_lazy('login user')



class UserLoginView(auth_views.LoginView):
    template_name = 'accounts/login_page.html'
    success_url = reverse_lazy('dashboard')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login user')
    return render(request, 'accounts/logout_page.html', {})



class ChangeUserPasswordView(auth_views.PasswordChangeView):
    template_name = 'accounts/change_password.html'
    success_url = reverse_lazy('password-change_done')


class ProfileDetailsView(auth_mixin.LoginRequiredMixin, views.DetailView):
    model = Profile
    template_name = 'profile_details.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cars = list(Car.objects.filter(user_id=self.object.user_id))
        #car_photos = CarPhoto.objects.filter(tagged_cars__in=cars).distinct()

      #  total_likes_count = sum(cp.likes for cp in car_photos)
       # total_car_photos_count = len(car_photos)

        context.update({
            #'total_likes_count': total_likes_count,
            #'total_car_photos_count': total_car_photos_count,
            'is_owner': self.object.user_id == self.request.user.id,
            'cars': cars,
        })

        return context


def edit_profile(request, pk):
    profile = Profile.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = EditProfileForm(instance=profile)
    context = {
        'form': form
    }
    return render(request, 'accounts/profile_edit.html', context)


def delete_profile(request, pk):
    profile = Profile.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home_pg')
    else:
        form = DeleteProfileForm(instance=profile)
    context = {
        'form': form
    }
    return render(request, 'accounts/profile_delete.html', context)