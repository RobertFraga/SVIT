# Generated by Django 4.2.17 on 2025-03-21 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_staff', '0031_rename_level_level_grade_remove_section_level_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='level',
            name='section_name',
        ),
        migrations.AddField(
            model_name='level',
            name='section_name',
            field=models.ManyToManyField(null=True, to='admin_staff.section'),
        ),
    ]
