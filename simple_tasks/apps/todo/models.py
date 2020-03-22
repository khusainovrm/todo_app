from django.db import models

# Create your models here.

class Card(models.Model):
    author = models.CharField(max_length=50)
    title = models.CharField("Заголовк", max_length=50)
    text = models.TextField("Текст")
    created = models.DateField(auto_now=True)
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