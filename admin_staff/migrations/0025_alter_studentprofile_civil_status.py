# Generated by Django 4.2.16 on 2024-10-31 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_staff', '0024_alter_studentprofile_civil_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='civil_status',
            field=models.CharField(choices=[('single', 'single'), ('married', 'married'), ('separated', 'separated'), ('divorced', 'divorced'), ('widowed', 'widowed')], default='civil_status', max_length=10, null=True),
        ),
    ]
