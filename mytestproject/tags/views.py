from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Tag
from .forms import TagForm

def get(request):
    tags = Tag.objects.all()
    return render(request, 'tags/tags.html', {'tags': tags})

def show(request, id):
    tag = get_object_or_404(Tag, pk=id)
    return render(request, 'tags/tag.html', {'tag': tag})

def delete(request, id):
    tag = get_object_or_404(Tag, pk=id)
    tag.delete()
    return redirect('tags')

def add(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tags')
    else:
        form = TagForm()
    return render(request, 'tags/tag_form.html', {
        'form': form,
        'title_page': 'Создать тег'
    })

def update(request, id):
    tag = get_object_or_404(Tag, pk=id)
    if request.method == 'POST':
        form = TagForm(request.POST, instance=tag)
        if form.is_valid():
            form.save()
            return redirect('tag', id=id)
    else:
        form = TagForm(instance=tag)
    return render(request, 'tags/tag_form.html', {
        'form': form,
        'title_page': 'Изменить тег'
    })