# Generated by Django 4.2.17 on 2025-04-01 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_staff', '0040_alter_studentprofile_student_lrn'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentprofile',
            name='ethnic_group',
        ),
        migrations.RemoveField(
            model_name='studentprofile',
            name='father_name',
        ),
        migrations.RemoveField(
            model_name='studentprofile',
            name='guardian_contact',
        ),
        migrations.RemoveField(
            model_name='studentprofile',
            name='guardian_name',
        ),
        migrations.RemoveField(
            model_name='studentprofile',
            name='mother_maide_name',
        ),
        migrations.RemoveField(
            model_name='studentprofile',
            name='mother_tongue',
        ),
        migrations.RemoveField(
            model_name='studentprofile',
            name='relationship',
        ),
    ]
