# Generated by Django 4.2.17 on 2025-04-08 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_staff', '0077_remove_studentprofile_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprofile',
            name='age',
            field=models.CharField(max_length=2, null=True),
        ),
    ]
