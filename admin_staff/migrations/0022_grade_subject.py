# Generated by Django 5.1.3 on 2024-11-26 09:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_staff', '0021_grade_facultystaff_grades'),
    ]

    operations = [
        migrations.AddField(
            model_name='grade',
            name='subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_staff.subject'),
        ),
    ]
