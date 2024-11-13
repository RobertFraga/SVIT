# Generated by Django 4.2.16 on 2024-11-12 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_staff', '0009_attendance'),
    ]

    operations = [
        migrations.DeleteModel(
            name='attendance',
        ),
        migrations.AddField(
            model_name='section',
            name='level',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='admin_staff.level'),
        ),
    ]
