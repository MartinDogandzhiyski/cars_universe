from django.shortcuts import redirect, render

from cars_universe.forms import CreateToolForm, EditToolForm, DeleteToolForm, CreatePartForm, EditPartForm, \
    DeletePartForm
from cars_universe.web.models.models import CarPart


def create_part(request):
    if request.user.is_staff:
        if request.method == 'POST':
            form = CreatePartForm(request.POST, request.FILES)

            if form.is_valid():
                form.save()
                return redirect('dashboard')
        else:
            form = CreatePartForm()
        context = {
            'form': form,
        }
        return render(request, 'part_create.html', context)


def edit_part(request, pk):
    if request.user.is_staff:
        instance = CarPart.objects.get(pk=pk)
        if request.method == 'POST':
            form = EditPartForm(request.POST, instance=instance)
            if form.is_valid():
                form.save()
                return redirect('parts')
        else:
            form = EditPartForm(instance=instance)

        context = {
            'form': form,
            'part': instance,
        }
        return render(request, 'part_edit.html', context)


def delete_part(request, pk):
    if request.user.is_staff:
        part = CarPart.objects.get(pk=pk)
        if request.method == 'POST':
            form = DeletePartForm(request.POST, instance=part)
            if form.is_valid():
                form.save()
                return redirect('parts')
        else:
            form = DeletePartForm(instance=part)
        context = {
            'form': form,
            'part': part,
        }
        return render(request, 'part_delete.html', context)