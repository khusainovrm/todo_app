from django.db import models
from django.utils import timezone

# Create your models here.

class Card(models.Model):
    author = models.CharField("Автор", max_length=50)
    title = models.CharField("Заголовк", max_length=50)
    text = models.CharField("Текст", max_length=50)
    created = models.DateTimeField(default=timezone.now)
    #color

    class Meta:
        ordering = ["-created"]
        verbose_name = "карточка"
        verbose_name_plural = "карточки"

    def __str__(self):
        return self.title

class Todo(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    text = models.TextField("Текст")

    def __str__(self):
        return self.text

    class Meta:
        ordering = ["-text"]
        verbose_name = "Список дел для карточек"
        verbose_name_plural = "Список дел для карточек"