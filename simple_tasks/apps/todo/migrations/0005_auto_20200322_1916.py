# Generated by Django 3.0.4 on 2020-03-22 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_auto_20200322_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='text',
            field=models.CharField(max_length=50, verbose_name='Текст'),
        ),
    ]
