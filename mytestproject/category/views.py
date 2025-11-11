from django.http import HttpResponse


from django.shortcuts import render, get_object_or_404, redirect
from .models import Categories
from .forms import CategoryForm
# Create your views here.


def categories(request): # получаем заметки из бд
   category = Categories.objects.all()
   # html = '<h1>Тут будут заметки</h1>'
   # for note in notes:
   #     #notes/note.id
   #     html += f'<a href = "{note.id}"><p>id = {note.id} title : {note.title} text:{note.body}</p></a>'
   return render(request,'category/categories.html', {'category_html':category})

def show(request,category_id):
    category = get_object_or_404(Categories,pk=category_id)
    #return HttpResponse(f'<h1> {note.title}</h1><p>{note.body}</p>')
    return render(request,'category/category.html', {'category_html':category})

# Метод отображает форму и добавляет и изменяет заметки в бд
def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST) # получает данные которые ввели в форму
        if form.is_valid():
            form.save() # Записывает данные таблицу в БД
            return redirect('category')
    else:
        form = CategoryForm()
    return render(request,'categories/forms_category.html',{
        'form': form, 'title_page': 'Создать категорию'
    })

def update(request,note_id):
    note = get_object_or_404(Categories,pk=note_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=note) # instance=note форма будет заполнена данными из таблиц
        if form.is_valid():
            form.save()
            return redirect('one_note', note_id=note_id)
    else:
        form = CategoryForm(instance=note)
    return render(request,'notes/forms.html',{
        'form':form, 'title_page': 'Изменить заметку'
    })


def delete(request,note_id):
    note = get_object_or_404(Categories, pk=note_id)
    note.delete()
    return redirect('notes')
