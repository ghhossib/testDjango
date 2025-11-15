from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Comment
from .forms import CommentForm

def get(request):
    comments = Comment.objects.all()
    return render(request, 'comments/comments.html', {'comments': comments})

def show(request, id):
    comment = get_object_or_404(Comment, pk=id)
    return render(request, 'comments/comments.html', {'comment': comment})

def delete(request, id):
    comment = get_object_or_404(Comment, pk=id)
    comment.delete()
    return redirect('comments')

def add(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('comments')
    else:
        form = CommentForm()
    return render(request, 'comments/comment_form.html', {
        'form': form,
        'title_page': 'Создать комментарий'
    })

def update(request, id):
    comment = get_object_or_404(Comment, pk=id)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('comment', id=id)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'comments/comment_form.html', {
        'form': form,
        'title_page': 'Изменить комментарий'
    })