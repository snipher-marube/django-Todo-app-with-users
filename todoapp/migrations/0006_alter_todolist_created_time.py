# Generated by Django 4.0.2 on 2022-03-06 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0005_alter_todolist_created_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='created_time',
            field=models.DateField(auto_now_add=True),
        ),
    ]