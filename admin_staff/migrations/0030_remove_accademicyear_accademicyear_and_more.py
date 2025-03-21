# Generated by Django 4.2.17 on 2025-03-21 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_staff', '0029_alter_accademicyear_accademicyear'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accademicyear',
            name='accademicYear',
        ),
        migrations.AddField(
            model_name='accademicyear',
            name='ending_year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='accademicyear',
            name='starting_year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
