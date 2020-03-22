from django.contrib import admin
from .models import Card, Todo

class CardAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'author','created']
    list_filter = ('author','title', 'created')
    search_fields = ('title', 'text')


admin.site.register(Card, CardAdmin)


admin.site.register(Todo)

