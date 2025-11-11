from django.http import HttpResponse

from .forms import NoteForm
from .models import Note
from django.shortcuts import render, get_object_or_404, redirect


# Create your views here.

def hello(request): #request - это объект запроса, вернуть ответ в виде объекта HTTP ответа
    return  HttpResponse('дароу')

def notes(request): # получаем заметки из бд
   notes = Note.objects.all()
   # html = '<h1>Тут будут заметки</h1>'
   # for note in notes:
   #     #notes/note.id
   #     html += f'<a href = "{note.id}"><p>id = {note.id} title : {note.title} text:{note.body}</p></a>'
   return render(request,'notes/notes.html', {'notes_html':notes})

def show(request,note_id):
    note = get_object_or_404(Note,pk=note_id)
    #return HttpResponse(f'<h1> {note.title}</h1><p>{note.body}</p>')
    return render(request,'notes/one.html', {'note_html':note})

# Метод отображает форму и добавляет и изменяет заметки в бд
def note_create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST) # получает данные которые ввели в форму
        if form.is_valid():
            form.save() # Записывает данные таблицу в БД
            return redirect('notes')
    else:
        form = NoteForm()
    return render(request,'notes/forms.html',{
        'form': form, 'title_page': 'Создать заметку'
    })

def update(request,note_id):
    note = get_object_or_404(Note,pk=note_id)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note) # instance=note форма будет заполнена данными из таблиц
        if form.is_valid():
            form.save()
            return redirect('one_note', note_id=note_id)
    else:
        form = NoteForm(instance=note)
    return render(request,'notes/forms.html',{
        'form':form, 'title_page': 'Изменить заметку'
    })


def delete(request,note_id):
    note = get_object_or_404(Note, pk=note_id)
    note.delete()
    return redirect('notes')
