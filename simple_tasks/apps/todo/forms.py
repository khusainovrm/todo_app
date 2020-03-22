from django import forms
from .models import Card, Todo

class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ["author", "title", "text"]

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["card", "text"]

