# Generated by Django 4.2.17 on 2025-04-02 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_staff', '0064_alter_studentprofile_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='birth_date',
            field=models.DateField(null=True),
        ),
    ]
