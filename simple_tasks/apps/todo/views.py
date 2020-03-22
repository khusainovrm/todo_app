from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse, redirect
from .models import Card
from .forms import CardForm, TodoForm


# Create your views here.

def home (request):
    all_notes = Card.objects.all()
    context = {
        "all_notes" : all_notes,
    }
    return render(request, 'todo/todo_list.html', context)

def todo_detail (request, note_id):
    todo=get_object_or_404(Card,id=note_id)
    todoes = todo.todo_set.all()
    context = {
        "todoes" : todoes,
        "todo": todo,
    }
    return render(request, 'todo/todo_detail.html', context)


def todo_create (request):
    if request.method == "POST":
        form=CardForm(request.POST)
        if form.is_valid():
            post = form.save (commit=False)
            post.save()
            return redirect ('todo:home')
    else:
        form = CardForm()
    context = {
        "form" : form
    }
    return render(request, "todo/todo_create.html", context)

def aim_create (request):
    form =TodoForm (request.POST or None)
    if form.is_valid ():
        form.save ()
        return HttpResponseRedirect (reverse ('todo:home'))
    context = {
        "form": form
    }
    return render (request, "todo/aim_create.html", context)