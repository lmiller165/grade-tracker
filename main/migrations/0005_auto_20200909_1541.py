# Generated by Django 3.1 on 2020-09-09 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_grades'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Grades',
            new_name='Grade',
        ),
    ]