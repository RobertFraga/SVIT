# Generated by Django 5.1.3 on 2024-11-23 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_staff', '0007_cashierstaff'),
    ]

    operations = [
        migrations.CreateModel(
            name='accademicYear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accademicYear', models.DateField(blank=True, null=True)),
            ],
        ),
    ]