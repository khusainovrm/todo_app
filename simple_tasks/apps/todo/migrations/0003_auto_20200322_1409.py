# Generated by Django 3.0.4 on 2020-03-22 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20200322_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]