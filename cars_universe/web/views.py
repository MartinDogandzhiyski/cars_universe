from django.shortcuts import render


def show_index(request):
    return render(request, 'home-no-profile.html')
