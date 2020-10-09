# Generated by Django 3.1 on 2020-10-07 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20200914_2006'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='ell_status',
            field=models.CharField(choices=[('EO', 'EO'), ('EL', 'EL'), ('RFEP', 'RFEP'), ('IFEP', 'IFEP'), ('N/A', 'N/A')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='grade_level',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='race',
            field=models.CharField(choices=[('american_indian_or_alaska_native', 'American Indian or Alaska Native'), ('asian', 'Asian'), ('black', 'Black'), ('latinx', 'Latinx'), ('native_hawaiian_or_pacific_islander', 'Native Hawaiin or Pacific Islander'), ('white', 'White'), ('other', 'Other')], max_length=50, null=True),
        ),
    ]
