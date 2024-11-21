# Generated by Django 5.1.3 on 2024-11-21 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_staff', '0004_registrarstaff_prefix'),
    ]

    operations = [
        migrations.AddField(
            model_name='facultystaff',
            name='sufix',
            field=models.CharField(blank=True, max_length=24, null=True),
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='sufix',
            field=models.CharField(blank=True, max_length=24, null=True),
        ),
        migrations.DeleteModel(
            name='registrarStaff',
        ),
    ]