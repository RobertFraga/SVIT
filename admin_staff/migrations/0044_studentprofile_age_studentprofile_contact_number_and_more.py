# Generated by Django 4.2.17 on 2025-04-02 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_staff', '0043_alter_studentprofile_adviser_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprofile',
            name='age',
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='contact_number',
            field=models.CharField(max_length=24, null=True),
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='ethnic_group',
            field=models.CharField(max_length=24, null=True),
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='fathers_last_name',
            field=models.CharField(max_length=24, null=True),
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='fathers_middle_name',
            field=models.CharField(max_length=24, null=True),
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='fathers_name',
            field=models.CharField(max_length=24, null=True),
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='guardian_last_name',
            field=models.CharField(blank=True, max_length=24),
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='guardian_middle_name',
            field=models.CharField(blank=True, max_length=24),
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='guardian_name',
            field=models.CharField(blank=True, max_length=24),
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='is_guardian',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='mother_tongue',
            field=models.CharField(max_length=24, null=True),
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='mothers_last_name',
            field=models.CharField(max_length=24, null=True),
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='mothers_middle_name',
            field=models.CharField(max_length=24, null=True),
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='mothers_name',
            field=models.CharField(max_length=24, null=True),
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='relationship',
            field=models.CharField(blank=24, max_length=24),
        ),
    ]
