# Generated by Django 3.1 on 2020-09-11 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20200911_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='profile_img',
            field=models.ImageField(default='default.jpg', upload_to='profile_imgs'),
        ),
    ]
