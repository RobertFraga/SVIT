# Generated by Django 5.1.3 on 2024-11-27 18:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_staff', '0024_studentprofile_grades'),
    ]

    operations = [
        migrations.AddField(
            model_name='grade',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='admin_staff.studentprofile'),
        ),
    ]
