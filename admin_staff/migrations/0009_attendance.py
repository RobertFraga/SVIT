# Generated by Django 4.2.16 on 2024-11-11 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_staff', '0008_facultystaff_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendance_date', models.DateField()),
            ],
            options={
                'db_table': 'attendance',
                'managed': False,
            },
        ),
    ]
