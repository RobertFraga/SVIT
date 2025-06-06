# Generated by Django 4.2.17 on 2025-04-02 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_staff', '0057_studentprofile_ethnic_group_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprofile',
            name='fathers_last_name',
            field=models.CharField(blank=True, max_length=24, null=True),
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='fathers_middle_name',
            field=models.CharField(blank=True, max_length=24, null=True),
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='fathers_name',
            field=models.CharField(blank=True, max_length=24, null=True),
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='mothers_last_name',
            field=models.CharField(blank=True, max_length=24, null=True),
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='mothers_middle_name',
            field=models.CharField(blank=True, max_length=24, null=True),
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='mothers_name',
            field=models.CharField(blank=True, max_length=24, null=True),
        ),
    ]
