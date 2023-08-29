from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404, redirect
from .models import NippoModel
from .forms import NippoFormsClass, ImageUploadForm
from django.views.generic.edit import CreateView
from django.views.generic import ListView

class NippoListView(ListView):
    template_name =  'nippo/nippo-list.html'

    def get_queryset(self):
        return NippoModel.objects.all()

def nippoDetailView(request, pk):
    template_name = 'nippo/nippo-detail.html'
    ctx = {}
    obj = get_object_or_404(NippoModel, pk=pk)
    ctx['object'] = obj

    return render(request, template_name, ctx)

def nippoCreateView(request):
    template_name = 'nippo/nippo-form.html'
    form = NippoFormsClass(request.POST or None)
    ctx = {'form': form}

    if form.is_valid():
        title = form.cleaned_data["title"]
        content = form.cleaned_data["content"]
        obj = NippoModel(title=title, content=content)
        obj.save()
        return redirect('nippo-list')

    return render(request, template_name, ctx)

def nippoUpdateView(request, pk):
    template_name = 'nippo/nippo-form.html'
    obj = get_object_or_404(NippoModel, pk=pk)
    initial_value = {'title': obj.title, 'content': obj.content}

    form = NippoFormsClass(request.POST or initial_value)
    ctx = {'form': form}
    ctx['object'] = obj

    if form.is_valid():
        obj.title = form.cleaned_data["title"]
        obj.content = form.cleaned_data["content"]
        obj.save()
        
        if request.POST:
            return redirect('nippo-list')

    return render(request, template_name, ctx)

def nippoDeleteView(request, pk):
    template_name = 'nippo/nippo-delete.html'
    obj = get_object_or_404(NippoModel, pk=pk)
    ctx = {'object': obj}

    if request.POST:
        obj.delete()
        return redirect('nippo-list')

    return render(request, template_name, ctx)

class ImageUploadView(CreateView):
    template_name = 'nippo/image-upload.html'
    form_class = ImageUploadForm
    success_url = '/'
