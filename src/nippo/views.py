from django.shortcuts import render, get_object_or_404
from .models import NippoModel
from .forms import NippoFormsClass

def nippoListView(request):
    template_name =  'nippo/nippo-list.html'
    ctx = {}
    obj_list = NippoModel.objects.all();
    ctx['obj_list'] = obj_list

    return render(request, template_name, ctx)

def nippoDetailView(request, pk):
    template_name = 'nippo/nippo-detail.html'
    ctx = {}
    obj = get_object_or_404(NippoModel, pk=pk)
    ctx['obj'] = obj

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

    return render(request, template_name, ctx)