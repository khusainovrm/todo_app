from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse
from .models import Card
from .forms import CardForm


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
    }
    return render(request, 'todo/todo_detail.html', context)


def todo_create (request):
    form=CardForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('todo:home'))
    context = {
        "form" : form
    }
    return render(request, "todo/todo_create.html", context)