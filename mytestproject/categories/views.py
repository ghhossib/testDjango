from django.http import HttpResponse


from django.shortcuts import render, get_object_or_404, redirect
from .models import Category
from .forms import CategoryForm
# Create your views here.


def get(request): # получаем заметки из бд
    categories = Category.objects.all()

    return render(request, 'categories/categories.html', {'categories':categories})


def show(request,id):
    category = get_object_or_404(Category,pk=id)
    #return HttpResponse(f'<h1> {note.title}</h1><p>{note.body}</p>')
    return render(request,'category/category.html', {'note_html':category})



def delete(request,id):
    category = get_object_or_404(Category, pk=id)
    category.delete()
    return redirect('categories')


def add(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
        form = CategoryForm()
    return render(request,'category/forms.html',{
        'form':form, 'title_page': 'Создать категорию'
    })

def update(request,id):
    category = get_object_or_404(Category,pk=id)
    if request.method == 'POST':
        form = CategoryForm(request.POST,instance=category)
        if form.is_valid():
            form.save()
            return redirect('category',id=id)
    else:
        form = CategoryForm()
    return render(request, 'category/forms.html', {
        'form': form, 'title_page': 'Изменить категорию'
    })
