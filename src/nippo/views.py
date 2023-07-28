from django.shortcuts import render
from random import randint
from .models import NippoModel

def nippoListView(request):
    template_name =  'nippo/nippo-list.html'
    ctx = {}
    obj_list = NippoModel.objects.all();
    ctx['obj_list'] = obj_list

    return render(request, template_name, ctx)

def nippoDetailView(request, pk):
    template_name = 'nippo/nippo-detail.html'
    ctx = {}
    obj = NippoModel.objects.get(pk=pk)
    ctx['obj'] = obj

    return render(request, template_name, ctx)

def nippoCreateView(request):
    template_name = 'nippo/nippo-form.html'

    if request.POST:
        title = request.POST['title']
        content = request.POST['content']

        obj = NippoModel(title=title, content=content)
        obj.save()

    return render(request, template_name)