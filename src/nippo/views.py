from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from .models import NippoModel
from .forms import NippoFormsClass, ImageUploadForm, NippoModelForm
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView, CreateView, UpdateView

class NippoListView(ListView):
    template_name =  'nippo/nippo-list.html'

    def get_queryset(self):
        return NippoModel.objects.all()

class NippoDetailView(DetailView):
    template_name = 'nippo/nippo-detail.html'
    model = NippoModel

class NippoCreateModelFormView(CreateView):
    template_name = 'nippo/nippo-form.html'
    form_class = NippoModelForm
    success_url = reverse_lazy('nippo-list')

class ImageUploadView(CreateView):
    template_name = 'nippo/image-upload.html'
    form_class = ImageUploadForm
    success_url = '/'

class NippoUpdateModelFormView(UpdateView):
    template_name = 'nippo/nippo-form.html'
    model = NippoModel
    form_class = NippoModelForm
    success_url = reverse_lazy('nippo-list')

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

