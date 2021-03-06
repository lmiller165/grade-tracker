# Generated by Django 3.1 on 2020-10-08 16:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade_level', models.IntegerField(null=True)),
                ('profile_img', models.ImageField(default='default.jpg', upload_to='profile_imgs')),
                ('calstudentID', models.IntegerField(null=True)),
                ('is_iep', models.BooleanField(default=False, null=True)),
                ('ell_status', models.CharField(choices=[('EO', 'EO'), ('EL', 'EL'), ('RFEP', 'RFEP'), ('IFEP', 'IFEP'), ('N/A', 'N/A')], max_length=50, null=True)),
                ('on_reduced_lunch', models.BooleanField(default=False, null=True)),
                ('race', models.CharField(choices=[('american_indian_or_alaska_native', 'American Indian or Alaska Native'), ('asian', 'Asian'), ('black', 'Black'), ('latinx', 'Latinx'), ('native_hawaiian_or_pacific_islander', 'Native Hawaiin or Pacific Islander'), ('white', 'White'), ('other', 'Other')], max_length=50, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
