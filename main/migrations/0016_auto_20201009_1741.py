# Generated by Django 3.1 on 2020-10-09 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20201008_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gpa',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]