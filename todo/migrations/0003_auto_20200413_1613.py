# Generated by Django 2.1 on 2020-04-13 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20200413_1606'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='todo_item',
            new_name='TodoItem',
        ),
    ]
