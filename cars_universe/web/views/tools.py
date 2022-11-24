from django.shortcuts import redirect, render

from cars_universe.forms import CreateToolForm, EditToolForm, DeleteToolForm
from cars_universe.web.models.models import Tool


def create_tool(request):
    if request.user.is_staff:
        if request.method == 'POST':
            form = CreateToolForm(request.POST, request.FILES)

            if form.is_valid():
                form.save()
                return redirect('dashboard')
        else:
            form = CreateToolForm()
        context = {
            'form': form,
        }
        return render(request, 'tool_create.html', context)


def edit_tool(request, pk):
    if request.user.is_staff:
        instance = Tool.objects.get(pk=pk)
        if request.method == 'POST':
            form = EditToolForm(request.POST, instance=instance)
            if form.is_valid():
                form.save()
                return redirect('tools')
        else:
            form = EditToolForm(instance=instance)

        context = {
            'form': form,
            'tool': instance,
        }
        return render(request, 'tool_edit.html', context)


def delete_tool(request, pk):
    if request.user.is_staff:
        tool = Tool.objects.get(pk=pk)
        if request.method == 'POST':
            form = DeleteToolForm(request.POST, instance=tool)
            if form.is_valid():
                form.save()
                return redirect('tools')
        else:
            form = DeleteToolForm(instance=tool)
        context = {
            'form': form,
            'tool': tool,
        }
        return render(request, 'tool_delete.html', context)