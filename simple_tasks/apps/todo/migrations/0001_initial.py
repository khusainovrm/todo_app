# Generated by Django 3.0.4 on 2020-03-22 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50, verbose_name='Заголовк')),
                ('text', models.TextField(verbose_name='Текст')),
                ('created', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name': 'карточка',
                'verbose_name_plural': 'карточки',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст')),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.Card')),
            ],
        ),
    ]
