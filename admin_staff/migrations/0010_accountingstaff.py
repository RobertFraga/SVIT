# Generated by Django 5.1.3 on 2024-11-23 11:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_staff', '0009_admissionstaff'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='accountingStaff',
            fields=[
                ('announting_staff_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('surname', models.CharField(max_length=24)),
                ('first_name', models.CharField(max_length=24)),
                ('middle_name', models.CharField(blank=True, max_length=24, null=True)),
                ('sufix', models.CharField(blank=True, max_length=24, null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Gender', max_length=10, null=True)),
                ('civil_status', models.CharField(blank=True, choices=[('Single', 'Single'), ('Married', 'Married'), ('Divorced', 'Divorced'), ('Widowed', 'Widowed')], default='Status', max_length=10, null=True)),
                ('birth_date', models.DateField(null=True)),
                ('birth_place', models.CharField(blank=True, max_length=200, null=True)),
                ('religion', models.CharField(blank=True, max_length=24, null=True)),
                ('contact', models.BigIntegerField(blank=True, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
