# Generated by Django 4.2.17 on 2025-04-02 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_staff', '0054_alter_studentprofile_is_guardian'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='is_guardian',
            field=models.BooleanField(default=False),
        ),
    ]
